# app/models.py
# Defines the database models — each class maps to a table in school.db.
# SQLAlchemy translates these Python classes into SQL tables automatically.

from flask_login import UserMixin
from app import db


# UserMixin adds the methods Flask-Login needs (is_authenticated, is_active, etc.)
class User(UserMixin, db.Model):
    """Represents a registered user of the site."""
    id            = db.Column(db.Integer, primary_key=True)   # unique ID, auto-incremented
    full_name     = db.Column(db.String(150), nullable=False)  # e.g. "María Fernández"
    email         = db.Column(db.String(150), unique=True, nullable=False)  # must be unique
    username      = db.Column(db.String(80),  unique=True, nullable=False)  # must be unique
    password_hash = db.Column(db.String(256), nullable=False)  # hashed — never plain text

    # One user can have one enrolment (uselist=False means it's a single object, not a list)
    enrolment = db.relationship("Enrolment", back_populates="user", uselist=False)


class Enrolment(db.Model):
    """Represents a course enrolment submitted by a user."""
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # links to User
    user_type   = db.Column(db.String(20), nullable=False)   # "argentina" or "international"
    course      = db.Column(db.String(100), nullable=False)  # course name selected at enrolment

    # Argentina-only fields (null for international students)
    cuit_cuil   = db.Column(db.String(20), nullable=True)
    dni         = db.Column(db.String(20), nullable=True)

    # International-only field (null for Argentine students)
    passport_no = db.Column(db.String(30), nullable=True)

    # Back-reference to the User who owns this enrolment
    user = db.relationship("User", back_populates="enrolment")
