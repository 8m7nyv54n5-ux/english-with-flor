# app/routes.py
# Contains the main blueprint — all the public-facing pages of the site.
# A blueprint is Flask's way of grouping related routes together.
# The auth routes (login, register, etc.) live separately in auth.py.

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from app.translations import TRANSLATIONS

# Create the "main" blueprint — registered with the app in __init__.py
main = Blueprint("main", __name__)


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
    return render_template("home.html", t=TRANSLATIONS[lang], lang=lang)


@main.route("/courses")
def courses():
    """Render the courses listing page (shows all three course cards)."""
    lang = get_lang()
    return render_template("courses.html", t=TRANSLATIONS[lang], lang=lang)


@main.route("/courses/beginner")
def course_beginner():
    """Render the Beginner course detail page.
    Builds a course dict from translation keys (beg_ prefix) and passes it
    to the shared course_detail.html template."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    course = {
        "title":        t["beg_title"],
        "level":        t["beg_level"],
        "tagline":      t["beg_tagline"],
        "who_title":    t["beg_who_title"],
        "who_desc":     t["beg_who_desc"],
        "learn_title":  t["beg_learn_title"],
        "learn_items":  t["beg_learn_items"],
        "format_title": t["beg_format_title"],
        "format_desc":  t["beg_format_desc"],
        "price_title":  t["beg_price_title"],
        "price_desc":   t["beg_price_desc"],
        "cta":          t["beg_cta"],
        "back":         t["beg_back"],
    }
    return render_template("course_detail.html", t=t, lang=lang, course=course)


@main.route("/courses/intermediate")
def course_intermediate():
    """Render the Intermediate course detail page.
    Builds a course dict from translation keys (int_ prefix)."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    course = {
        "title":        t["int_title"],
        "level":        t["int_level"],
        "tagline":      t["int_tagline"],
        "who_title":    t["int_who_title"],
        "who_desc":     t["int_who_desc"],
        "learn_title":  t["int_learn_title"],
        "learn_items":  t["int_learn_items"],
        "format_title": t["int_format_title"],
        "format_desc":  t["int_format_desc"],
        "price_title":  t["int_price_title"],
        "price_desc":   t["int_price_desc"],
        "cta":          t["int_cta"],
        "back":         t["int_back"],
    }
    return render_template("course_detail.html", t=t, lang=lang, course=course)


@main.route("/courses/advanced")
def course_advanced():
    """Render the Advanced course detail page.
    Builds a course dict from translation keys (adv_ prefix)."""
    lang = get_lang()
    t = TRANSLATIONS[lang]
    course = {
        "title":        t["adv_title"],
        "level":        t["adv_level"],
        "tagline":      t["adv_tagline"],
        "who_title":    t["adv_who_title"],
        "who_desc":     t["adv_who_desc"],
        "learn_title":  t["adv_learn_title"],
        "learn_items":  t["adv_learn_items"],
        "format_title": t["adv_format_title"],
        "format_desc":  t["adv_format_desc"],
        "price_title":  t["adv_price_title"],
        "price_desc":   t["adv_price_desc"],
        "cta":          t["adv_cta"],
        "back":         t["adv_back"],
    }
    return render_template("course_detail.html", t=t, lang=lang, course=course)


@main.route("/about")
def about():
    """Render the About page."""
    lang = get_lang()
    return render_template("about.html", t=TRANSLATIONS[lang], lang=lang)


@main.route("/contact")
def contact():
    """Render the Contact page."""
    lang = get_lang()
    return render_template("contact.html", t=TRANSLATIONS[lang], lang=lang)


@main.route("/dashboard")
@login_required  # redirects to login page if the user is not logged in
def dashboard():
    """Render the logged-in user's dashboard, showing their details and enrolment."""
    lang = get_lang()
    return render_template("dashboard.html", t=TRANSLATIONS[lang], lang=lang, user=current_user)
