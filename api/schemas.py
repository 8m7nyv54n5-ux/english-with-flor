# api/schemas.py
# Pydantic models that define the shape of API request and response data.
# FastAPI uses these to validate data and auto-generate documentation.

from pydantic import BaseModel


# CourseSummary defines what a course looks like in a list response.
# Each field has a type hint — Pydantic enforces these automatically.
class CourseSummary(BaseModel):
    level: str      # e.g. "A1", "A2", "B1"
    title: str      # e.g. "Complete Beginner"
    tagline: str    # short description
    price: str      # e.g. "ARS 15,000 / month"


# CourseDetail is returned by GET /courses/{level}.
# It extends CourseSummary with the richer fields from the course detail page.
class CourseDetail(CourseSummary):
    who_desc: str       # who the course is for
    learn_items: list[str]  # bullet points of what students will learn
    format_desc: str    # how lessons are delivered


# WordOfDay defines the shape of the /word-of-the-day response.
class WordOfDay(BaseModel):
    label: str          # "Word of the Day" / "Palabra del día"
    word: str
    phonetic: str
    part_of_speech: str
    definition: str
    example: str


# EnquiryIn defines what the client must send in the POST /enquiries request body.
# Pydantic validates all fields automatically — missing or wrong types get a 422 error.
class EnquiryIn(BaseModel):
    name: str
    email: str
    message: str


# EnquiryOut defines what we send back to the client after receiving an enquiry.
# It extends EnquiryIn (echoing back what was sent) and adds server-generated fields.
class EnquiryOut(EnquiryIn):
    received_at: str    # ISO timestamp of when the enquiry was received
    confirmation: str   # Human-readable confirmation message
