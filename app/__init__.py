# app/__init__.py
# This file is the app factory — it creates and configures the Flask application.
# Using a factory function (create_app) instead of a global app object makes
# the app easier to test and configure for different environments.

import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from app.translations import TRANSLATIONS

# Load environment variables from the .env file into os.environ
# This is how we read the SECRET_KEY without hardcoding it
load_dotenv()

# Create extension objects without binding them to an app yet.
# They get properly initialised inside create_app() via .init_app().
db = SQLAlchemy()           # handles all database operations
login_manager = LoginManager()  # tracks who is logged in
csrf = CSRFProtect()        # makes csrf_token() available in all templates
limiter = Limiter(key_func=get_remote_address)  # rate-limits routes by IP address


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # SECRET_KEY is used to sign session cookies — keep it secret in production.
    # If the key is missing the app refuses to start, so you notice immediately
    # rather than silently running with a guessable fallback.
    secret_key = os.environ.get("SECRET_KEY")
    if not secret_key:
        raise RuntimeError("SECRET_KEY is not set — add it to your .env file")
    app.config["SECRET_KEY"] = secret_key
    # Tell SQLAlchemy to use a SQLite file called school.db inside the instance/ folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db"
    # SESSION_COOKIE_SECURE: only transmit the session cookie over HTTPS.
    # Set SESSION_COOKIE_SECURE=true in the production .env (PythonAnywhere).
    # Leave unset for local dev — HTTPS isn't available on 127.0.0.1.
    app.config["SESSION_COOKIE_SECURE"]   = os.environ.get("SESSION_COOKIE_SECURE", "false").lower() == "true"
    # SameSite=Lax stops the session cookie being sent with cross-site requests,
    # which provides CSRF protection as a second layer on top of Flask-WTF tokens.
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    # Bind the extensions to this specific app instance
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    # If a user tries to visit a @login_required page, redirect them to the login route
    login_manager.login_view = "auth.login"

    # Register blueprints — each blueprint is a group of related routes
    from app.routes import main
    from app.auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    # Create all database tables if they don't already exist
    from app import models
    with app.app_context():
        db.create_all()

    # Add security headers to every response.
    # These tell the browser to enable built-in protections.
    @app.after_request
    def set_security_headers(response):
        # Prevents the browser guessing the content type (stops MIME-sniffing attacks)
        response.headers["X-Content-Type-Options"] = "nosniff"
        # Stops the site being loaded inside an <iframe> on another domain (clickjacking)
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        # Content Security Policy — controls which resources the browser is allowed to load.
        # 'unsafe-inline' is needed for the inline <script> and style= attributes in templates.
        # Google Fonts domains are whitelisted for the stylesheet and font files.
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline'; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' data:; "
            "frame-ancestors 'self';"
        )
        return response

    # Custom error pages — show friendly pages instead of Flask's defaults.
    # Each handler reads the ?lang= parameter so the error page matches
    # the language the visitor was browsing in.
    @app.errorhandler(404)
    def page_not_found(error):
        lang = request.args.get("lang", "en")
        if lang not in TRANSLATIONS:
            lang = "en"
        t = TRANSLATIONS[lang]
        return render_template("404.html", t=t, lang=lang), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        lang = request.args.get("lang", "en")
        if lang not in TRANSLATIONS:
            lang = "en"
        t = TRANSLATIONS[lang]
        return render_template("500.html", t=t, lang=lang), 500

    return app


# This function tells Flask-Login how to reload a user from the database
# given their user ID, which is stored in the session cookie.
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))
