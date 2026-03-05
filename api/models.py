# api/models.py
# Standalone SQLAlchemy model for the FastAPI app.
#
# The Flask app's models use Flask-SQLAlchemy and Flask-Login, both of which
# require an active Flask application context. Since FastAPI has no such context,
# we define a plain SQLAlchemy model here instead.
#
# This model maps to the existing "user" table in school.db — it does not create
# a new table. Only the columns needed by the API are declared; SQLAlchemy
# silently ignores any additional columns present in the real table.

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    """Maps to the 'user' table created by the Flask app."""
    __tablename__ = "user"

    id            = Column(Integer, primary_key=True)
    username      = Column(String(80),  unique=True, nullable=False)
    email         = Column(String(150), unique=True, nullable=False)
    first_name    = Column(String(80),  nullable=False)
    last_name     = Column(String(80),  nullable=False)
    password_hash = Column(String(256), nullable=False)
    is_admin      = Column(Boolean, default=False)
