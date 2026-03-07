# api/schemas.py
# Pydantic models defining the shape of all API request and response bodies.
# FastAPI uses these for automatic validation and Swagger documentation.

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CourseSummary(BaseModel):
    level: str
    title: str
    tagline: str
    price: str


# Extends CourseSummary with the additional fields returned by GET /courses/{level}.
class CourseDetail(CourseSummary):
    who_desc: str
    learn_items: list[str]
    format_desc: str


class WordOfDay(BaseModel):
    label: str          # Localised label: "Word of the Day" / "Palabra del día"
    word: str
    phonetic: str
    part_of_speech: str
    definition: str
    example: str


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str     # Always "bearer"


# from_attributes=True allows Pydantic to read values directly from SQLAlchemy
# model instances (ORM objects) rather than requiring a plain dict.
class UserProfile(BaseModel):
    username:   str
    email:      str
    first_name: str
    last_name:  str
    is_admin:   bool

    model_config = {"from_attributes": True}


# Both fields are Optional so clients can update one or both in a single request.
class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name:  Optional[str] = None


class EnquiryIn(BaseModel):
    name: str
    email: str
    message: str


# from_attributes=True lets Pydantic read from a SQLAlchemy model instance (not just a dict).
# received_at is a datetime object from the DB — Pydantic serialises it to ISO 8601 automatically.
class EnquiryOut(BaseModel):
    id:           int
    name:         str
    email:        str
    message:      str
    received_at:  datetime
    confirmation: str

    model_config = {"from_attributes": True}
