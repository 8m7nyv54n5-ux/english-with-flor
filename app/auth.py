# app/auth.py
# Contains the auth blueprint — all routes related to user accounts:
# registering, logging in, logging out, and enrolling on a course.

from functools import wraps
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, limiter
from app.models import User, Enrolment, ContactMessage
from app.forms import (RegistrationForm, LoginForm, EnrolmentForm,
                       EditProfileForm, EditAddressForm, ChangePasswordForm, DeleteAccountForm)
from app.translations import TRANSLATIONS
from app.routes import SHOW_C_LEVELS

# Create the "auth" blueprint — registered with the app in __init__.py
auth = Blueprint("auth", __name__)


def admin_required(f):
    """Decorator that restricts a route to admin users only.
    Works like @login_required but also checks is_admin.
    Usage: stack it below @login_required on any admin route."""
    @wraps(f)  # preserves the original function's name and docstring
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            flash("You don't have permission to view that page.")
            return redirect(url_for("main.home"))
        return f(*args, **kwargs)
    return decorated


def get_lang():
    """Read the ?lang= URL parameter and return a valid language code.
    Defaults to English if the parameter is missing or unrecognised."""
    lang = request.args.get("lang", "en")
    if lang not in TRANSLATIONS:
        lang = "en"
    return lang


@auth.route("/register", methods=["GET", "POST"])
@limiter.limit("10 per minute")  # prevent mass fake-account creation
def register():
    """Handle new user registration.
    GET  — display the blank registration form.
    POST — validate the form, create the user, and redirect to enrolment."""
    lang = get_lang()
    form = RegistrationForm()

    if form.validate_on_submit():
        # Check username and email are not already taken.
        # Both checks use the same generic message so attackers can't tell
        # which field is already registered (prevents account enumeration).
        if (User.query.filter_by(username=form.username.data).first() or
                User.query.filter_by(email=form.email.data).first()):
            flash(TRANSLATIONS[lang]["error_account_exists"])
            return render_template("register.html", form=form, t=TRANSLATIONS[lang], lang=lang)

        # Hash the password — never store plain text.
        # Specifying "scrypt" explicitly so a future Werkzeug update can't
        # silently switch to a weaker default algorithm.
        hashed_password = generate_password_hash(form.password.data, method="scrypt")

        # Create the new User object and save it to the database
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            username=form.username.data,
            password_hash=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        # Auto log in and send to the dashboard
        login_user(user)
        return redirect(url_for("main.dashboard", lang=lang))

    return render_template("register.html", form=form, t=TRANSLATIONS[lang], lang=lang)


@auth.route("/login", methods=["GET", "POST"])
@limiter.limit("10 per minute")  # block brute-force attempts — max 10 login tries per minute per IP
def login():
    """Handle user login.
    GET  — display the login form.
    POST — check credentials and log the user in if correct."""
    lang = get_lang()
    form = LoginForm()

    if form.validate_on_submit():
        # Look up the user by username
        user = User.query.filter_by(username=form.username.data).first()

        # check_password_hash compares the submitted password against the stored hash
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for("main.home", lang=lang))

        # Show a generic error — don't reveal whether username or password was wrong
        flash(TRANSLATIONS[lang]["error_invalid_credentials"])

    return render_template("login.html", form=form, t=TRANSLATIONS[lang], lang=lang)


@auth.route("/logout", methods=["POST"])
@login_required  # must be logged in to log out
def logout():
    """Log the current user out and redirect to the home page.
    Uses POST (not GET) so that a malicious site can't log a user out
    by tricking their browser into making a GET request (e.g. via an <img> tag)."""
    lang = get_lang()
    logout_user()
    return redirect(url_for("main.home", lang=lang))


@auth.route("/enrol", methods=["GET", "POST"])
@login_required  # must be logged in to enrol
def enrol():
    """Handle course enrolment.
    GET  — display the enrolment form.
    POST — validate, save the enrolment, and redirect to dashboard."""
    lang = get_lang()

    # Guard: redirect if the user is already enrolled — prevents duplicate records
    if current_user.enrolment:
        return redirect(url_for("main.dashboard", lang=lang))

    form = EnrolmentForm()

    # Only show C1/C2 in the dropdown when the feature flag is on.
    # This keeps the enrolment form in sync with the courses page.
    allowed_courses = [
        ("a1", "A1 English"), ("a2", "A2 English"),
        ("b1", "B1 English"), ("b2", "B2 English"),
    ]
    if SHOW_C_LEVELS:
        allowed_courses += [("c1", "C1 English"), ("c2", "C2 English")]
    form.course.choices = allowed_courses

    if form.validate_on_submit():
        user_type = form.user_type.data

        # Validate the relevant fields based on whether the student is Argentine or international
        if user_type == "argentina":
            if not form.cuit_cuil.data or not form.dni.data:
                flash(TRANSLATIONS[lang]["error_argentina_fields"])
                return render_template("enrol.html", form=form, t=TRANSLATIONS[lang], lang=lang)
        else:
            if not form.passport_no.data:
                flash(TRANSLATIONS[lang]["error_passport_required"])
                return render_template("enrol.html", form=form, t=TRANSLATIONS[lang], lang=lang)

        # Create the Enrolment record and link it to the logged-in user
        enrolment = Enrolment(
            user_id=current_user.id,
            user_type=user_type,
            course=form.course.data,
            cuit_cuil=form.cuit_cuil.data or None,   # store None if field was left blank
            dni=form.dni.data or None,
            passport_no=form.passport_no.data or None,
            address_line=form.address_line.data,
            city=form.city.data,
            province=form.province.data,
            country=form.country.data,
            postcode=form.postcode.data
        )
        db.session.add(enrolment)
        db.session.commit()

        return redirect(url_for("main.dashboard", lang=lang))

    return render_template("enrol.html", form=form, t=TRANSLATIONS[lang], lang=lang)


@auth.route("/edit-profile", methods=["GET", "POST"])
@login_required  # must be logged in to edit your own profile
def edit_profile():
    """Let the user update their first name, last name, and email.
    GET  — display the form pre-filled with current values.
    POST — validate, check for duplicate email, save changes."""
    lang = get_lang()
    t = TRANSLATIONS[lang]

    # Pre-fill the form with the user's current details.
    # obj=current_user tells WTForms to populate fields from the User object.
    form = EditProfileForm(obj=current_user)

    if form.validate_on_submit():
        # If the email has changed, check it's not already taken by someone else
        new_email = form.email.data
        if new_email != current_user.email:
            if User.query.filter_by(email=new_email).first():
                flash(t["error_email_taken"])
                return render_template("edit_profile.html", form=form, t=t, lang=lang)

        # Update the user's details in the database
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = new_email
        db.session.commit()

        flash(t["edit_profile_success"], "success")
        return redirect(url_for("main.dashboard", lang=lang))

    return render_template("edit_profile.html", form=form, t=t, lang=lang)


@auth.route("/edit-address", methods=["GET", "POST"])
@login_required  # must be logged in to edit your own address
def edit_address():
    """Let the user update their address details.
    Only accessible if the user has already enrolled (address lives on Enrolment).
    GET  — display the form pre-filled with current address.
    POST — validate and save changes."""
    lang = get_lang()
    t = TRANSLATIONS[lang]

    # Guard: if user hasn't enrolled yet, there's no address to edit
    if not current_user.enrolment:
        return redirect(url_for("main.dashboard", lang=lang))

    # obj=current_user.enrolment pre-fills form fields from the Enrolment object
    form = EditAddressForm(obj=current_user.enrolment)

    if form.validate_on_submit():
        current_user.enrolment.address_line = form.address_line.data
        current_user.enrolment.city         = form.city.data
        current_user.enrolment.province     = form.province.data
        current_user.enrolment.country      = form.country.data
        current_user.enrolment.postcode     = form.postcode.data
        db.session.commit()

        flash(t["edit_address_success"], "success")
        return redirect(url_for("main.dashboard", lang=lang))

    return render_template("edit_address.html", form=form, t=t, lang=lang)


@auth.route("/change-password", methods=["GET", "POST"])
@login_required  # must be logged in to change your own password
def change_password():
    """Let the user change their password.
    Requires the current password for verification before accepting a new one.
    The new password is hashed with scrypt before saving — same as registration."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    form = ChangePasswordForm()

    if form.validate_on_submit():
        # Verify the current password is correct before allowing a change
        if not check_password_hash(current_user.password_hash, form.current_password.data):
            flash(t["error_wrong_password"])
            return render_template("change_password.html", form=form, t=t, lang=lang)

        # Hash the new password and save it
        current_user.password_hash = generate_password_hash(
            form.new_password.data, method="scrypt"
        )
        db.session.commit()

        flash(t["change_pw_success"], "success")
        return redirect(url_for("main.dashboard", lang=lang))

    return render_template("change_password.html", form=form, t=t, lang=lang)


@auth.route("/delete-account", methods=["GET", "POST"])
@login_required  # must be logged in to delete your own account
def delete_account():
    """Let the user permanently delete their account.
    Requires password confirmation to prevent accidental deletion.
    Deletes the enrolment first (foreign key) then the user record."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    form = DeleteAccountForm()

    if form.validate_on_submit():
        # Verify the password before allowing deletion
        if not check_password_hash(current_user.password_hash, form.password.data):
            flash(t["error_wrong_password"])
            return render_template("delete_account.html", form=form, t=t, lang=lang)

        # Delete the enrolment first (foreign key references the user)
        if current_user.enrolment:
            db.session.delete(current_user.enrolment)

        # Delete the user record itself
        db.session.delete(current_user)
        db.session.commit()

        # Log the user out — their session is no longer valid
        logout_user()

        flash(t["delete_account_success"], "success")
        return redirect(url_for("main.home", lang=lang))

    return render_template("delete_account.html", form=form, t=t, lang=lang)


@auth.route("/admin")
@login_required   # step 1: must be logged in
@admin_required   # step 2: must also be an admin
def admin():
    """Render the admin dashboard — visible to Flor only.
    Queries all users, enrolments, and contact messages from the database."""
    lang = get_lang()
    # Fetch all records from each table, ordered newest first for messages
    users    = User.query.order_by(User.id).all()
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template("admin.html", users=users, messages=messages, t=TRANSLATIONS[lang], lang=lang)
