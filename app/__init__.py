# app/__init__.py
# This file is the app factory — it creates and configures the Flask application.
# Using a factory function (create_app) instead of a global app object makes
# the app easier to test and configure for different environments.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv

# Load environment variables from the .env file into os.environ
# This is how we read the SECRET_KEY without hardcoding it
load_dotenv()

# Create extension objects without binding them to an app yet.
# They get properly initialised inside create_app() via .init_app().
db = SQLAlchemy()           # handles all database operations
login_manager = LoginManager()  # tracks who is logged in
limiter = Limiter(key_func=get_remote_address)  # rate-limits routes by IP address


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # SECRET_KEY is used to sign session cookies — keep it secret in production
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-in-production")
    # Tell SQLAlchemy to use a SQLite file called school.db inside the instance/ folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db"

    # Bind the extensions to this specific app instance
    db.init_app(app)
    login_manager.init_app(app)
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

    return app


# This function tells Flask-Login how to reload a user from the database
# given their user ID, which is stored in the session cookie.
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))
