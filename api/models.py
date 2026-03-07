# api/models.py
# Standalone SQLAlchemy models for the FastAPI app.
#
# The Flask app's models use Flask-SQLAlchemy and Flask-Login, both of which
# require an active Flask application context. Since FastAPI has no such context,
# we define plain SQLAlchemy models here instead.
#
# User maps to the existing "user" table created by the Flask app — only the
# columns needed by the API are declared; SQLAlchemy silently ignores any
# additional columns present in the real table.
#
# Enquiry is a new table created by FastAPI on startup via Base.metadata.create_all().

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone


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


class Enquiry(Base):
    """Stores incoming enquiries from prospective students."""
    __tablename__ = "enquiry"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(120),  nullable=False)
    email       = Column(String(150),  nullable=False)
    message     = Column(String(2000), nullable=False)
    # Default is a lambda so the timestamp is evaluated at insert time, not at class definition time.
    received_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
