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
