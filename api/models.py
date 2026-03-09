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

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
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


class Enrolment(Base):
    """Maps to the 'enrolment' table created by the Flask app."""
    __tablename__ = "enrolment"

    id           = Column(Integer, primary_key=True)
    user_id      = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_type    = Column(String(20),  nullable=False)   # "argentina" or "international"
    course       = Column(String(100), nullable=False)

    # Argentina-only (null for international students)
    cuit_cuil    = Column(String(20),  nullable=True)
    dni          = Column(String(20),  nullable=True)

    # International-only (null for Argentine students)
    passport_no  = Column(String(30),  nullable=True)

    # Address fields — required for all students
    address_line = Column(String(200), nullable=False)
    city         = Column(String(100), nullable=False)
    province     = Column(String(100), nullable=False)
    country      = Column(String(100), nullable=False)
    postcode     = Column(String(20),  nullable=False)


class Enquiry(Base):
    """Stores incoming enquiries from prospective students."""
    __tablename__ = "enquiry"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(120),  nullable=False)
    email       = Column(String(150),  nullable=False)
    message     = Column(String(2000), nullable=False)
    # Default is a lambda so the timestamp is evaluated at insert time, not at class definition time.
    received_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
