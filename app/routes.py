# app/routes.py
# Contains the main blueprint — all the public-facing pages of the site.
# A blueprint is Flask's way of grouping related routes together.
# The auth routes (login, register, etc.) live separately in auth.py.

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.translations import TRANSLATIONS
from app.forms import ContactForm
from app.models import ContactMessage
from app import db, limiter
from datetime import date
from app.words import WORDS

# Create the "main" blueprint — registered with the app in __init__.py
main = Blueprint("main", __name__)
# Feature flag — set to True when C1 and C2 courses are ready to go live
SHOW_C_LEVELS = False

def get_lang():
    """Read the ?lang= URL parameter and return a valid language code.
    Defaults to English if the parameter is missing or unrecognised."""
    lang = request.args.get("lang", "en")
    if lang not in TRANSLATIONS:
        lang = "en"
    return lang


@main.route("/")
def home():
    """Render the home page with the correct language."""
    lang = get_lang()
    day_index = date.today().toordinal() % len(WORDS)  # changes daily
    word_of_day = WORDS[day_index]
    return render_template("home.html", t=TRANSLATIONS[lang], lang=lang, show_c_levels=SHOW_C_LEVELS, word=word_of_day)



@main.route("/courses")
def courses():
    """Render the courses listing page (shows all three course cards)."""
    lang = get_lang()
    return render_template("courses.html", t=TRANSLATIONS[lang], lang=lang, show_c_levels=SHOW_C_LEVELS)


def build_course(t, prefix):
    """Helper that builds a course dict from translation keys using a given prefix.
    For example, build_course(t, 'a1') pulls all keys starting with 'a1_'.
    This avoids repeating the same dict structure 6 times."""
    return {
        "title":        t[f"{prefix}_title"],
        "level":        t[f"{prefix}_level"],
        "tagline":      t[f"{prefix}_tagline"],
        "who_title":    t[f"{prefix}_who_title"],
        "who_desc":     t[f"{prefix}_who_desc"],
        "learn_title":  t[f"{prefix}_learn_title"],
        "learn_items":  t[f"{prefix}_learn_items"],
        "format_title": t[f"{prefix}_format_title"],
        "format_desc":  t[f"{prefix}_format_desc"],
        "price_title":  t[f"{prefix}_price_title"],
        "price_desc":   t[f"{prefix}_price_desc"],
        "cta":          t[f"{prefix}_cta"],
        "back":         t[f"{prefix}_back"],
    }


@main.route("/courses/a1")
def course_a1():
    """Render the A1 course detail page."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    return render_template("course_detail.html", t=t, lang=lang, course=build_course(t, "a1"))


@main.route("/courses/a2")
def course_a2():
    """Render the A2 course detail page."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    return render_template("course_detail.html", t=t, lang=lang, course=build_course(t, "a2"))


@main.route("/courses/b1")
def course_b1():
    """Render the B1 course detail page."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    return render_template("course_detail.html", t=t, lang=lang, course=build_course(t, "b1"))


@main.route("/courses/b2")
def course_b2():
    """Render the B2 course detail page."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    return render_template("course_detail.html", t=t, lang=lang, course=build_course(t, "b2"))


@main.route("/courses/c1")
def course_c1():
    """Render the C1 course detail page."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    return render_template("course_detail.html", t=t, lang=lang, course=build_course(t, "c1"))


@main.route("/courses/c2")
def course_c2():
    """Render the C2 course detail page."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    return render_template("course_detail.html", t=t, lang=lang, course=build_course(t, "c2"))


@main.route("/about")
def about():
    """Render the About page."""
    lang = get_lang()
    return render_template("about.html", t=TRANSLATIONS[lang], lang=lang)


@main.route("/contact", methods=["GET", "POST"])
@limiter.limit("5 per minute")  # prevent spam — max 5 contact submissions per minute per IP
def contact():
    """Render the Contact page. On POST, save the message to the database."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    form = ContactForm()

    if form.validate_on_submit():
        # Save the message to the database
        msg = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data,
        )
        db.session.add(msg)
        db.session.commit()
        flash(t["contact_success"], "success")
        return redirect(url_for("main.contact", lang=lang))

    return render_template("contact.html", t=t, lang=lang, form=form)


@main.route("/dashboard")
@login_required  # redirects to login page if the user is not logged in
def dashboard():
    """Render the logged-in user's dashboard, showing their details and enrolment."""
    lang = get_lang()
    return render_template("dashboard.html", t=TRANSLATIONS[lang], lang=lang, user=current_user)
