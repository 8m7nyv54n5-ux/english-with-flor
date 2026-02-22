# app/auth.py
# Contains the auth blueprint — all routes related to user accounts:
# registering, logging in, logging out, and enrolling on a course.

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, limiter
from app.models import User, Enrolment
from app.forms import RegistrationForm, LoginForm, EnrolmentForm
from app.translations import TRANSLATIONS

# Create the "auth" blueprint — registered with the app in __init__.py
auth = Blueprint("auth", __name__)


def get_lang():
    """Read the ?lang= URL parameter and return a valid language code.
    Defaults to English if the parameter is missing or unrecognised."""
    lang = request.args.get("lang", "en")
    if lang not in TRANSLATIONS:
        lang = "en"
    return lang


@auth.route("/register", methods=["GET", "POST"])
def register():
    """Handle new user registration.
    GET  — display the blank registration form.
    POST — validate the form, create the user, and redirect to enrolment."""
    lang = get_lang()
    form = RegistrationForm()

    if form.validate_on_submit():
        # Check username and email are not already taken
        if User.query.filter_by(username=form.username.data).first():
            flash(TRANSLATIONS[lang]["error_username_taken"])
            return render_template("register.html", form=form, t=TRANSLATIONS[lang], lang=lang)

        if User.query.filter_by(email=form.email.data).first():
            flash(TRANSLATIONS[lang]["error_email_taken"])
            return render_template("register.html", form=form, t=TRANSLATIONS[lang], lang=lang)

        # Hash the password — never store plain text
        hashed_password = generate_password_hash(form.password.data)

        # Create the new User object and save it to the database
        user = User(
            full_name=form.full_name.data,
            email=form.email.data,
            username=form.username.data,
            password_hash=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        # Auto log in and send straight to enrolment
        login_user(user)
        return redirect(url_for("auth.enrol", lang=lang))

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


@auth.route("/logout")
@login_required  # must be logged in to log out
def logout():
    """Log the current user out and redirect to the home page."""
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
    form = EnrolmentForm()

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
            passport_no=form.passport_no.data or None
        )
        db.session.add(enrolment)
        db.session.commit()

        return redirect(url_for("main.dashboard", lang=lang))

    return render_template("enrol.html", form=form, t=TRANSLATIONS[lang], lang=lang)
