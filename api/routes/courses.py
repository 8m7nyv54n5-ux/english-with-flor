# api/routes/courses.py
# Handles course-related endpoints.

from fastapi import APIRouter, HTTPException
from api.schemas import CourseSummary, CourseDetail
import sys, os

# Add project root to path so we can import from app/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))
from app.translations import TRANSLATIONS

router = APIRouter()

# Hardcoded list of active course levels (mirrors SHOW_C_LEVELS logic in Flask app)
ACTIVE_LEVELS = ["a1", "a2", "b1", "b2"]


# response_model=list[CourseSummary] tells FastAPI:
# - validate that what we return matches CourseSummary
# - document this shape in /docs automatically
@router.get("/courses", response_model=list[CourseSummary])
def get_courses():
    """Return a summary list of all active courses."""
    t = TRANSLATIONS["en"]
    courses = []

    for level in ACTIVE_LEVELS:
        courses.append({
            "level":   t[f"{level}_level"],
            "title":   t[f"{level}_title"],
            "tagline": t[f"{level}_tagline"],
            "price":   t[f"{level}_price_desc"],
        })

    return courses


# {level} in the path is a path parameter — FastAPI captures it from the URL
# and passes it into the function as the `level` argument.
# response_model=CourseDetail tells FastAPI to validate and document the richer schema.
@router.get("/courses/{level}", response_model=CourseDetail)
def get_course(level: str):
    """Return full details for a single course by CEFR level (e.g. 'b1')."""
    # Normalise to lowercase so /courses/B1 and /courses/b1 both work
    level = level.lower()

    # Return 404 if the level doesn't exist or isn't active yet
    if level not in ACTIVE_LEVELS:
        raise HTTPException(status_code=404, detail=f"Course '{level}' not found")

    t = TRANSLATIONS["en"]

    return {
        "level":        t[f"{level}_level"],
        "title":        t[f"{level}_title"],
        "tagline":      t[f"{level}_tagline"],
        "price":        t[f"{level}_price_desc"],
        "who_desc":     t[f"{level}_who_desc"],
        "learn_items":  t[f"{level}_learn_items"],
        "format_desc":  t[f"{level}_format_desc"],
    }
