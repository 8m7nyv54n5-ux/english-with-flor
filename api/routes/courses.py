# api/routes/courses.py
# Course endpoints: GET /courses and GET /courses/{level}.
# Reads from the shared translations dictionary to avoid duplicating course content.

from fastapi import APIRouter, HTTPException
from api.schemas import CourseSummary, CourseDetail
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))
from app.translations import TRANSLATIONS

router = APIRouter()

# Mirrors the SHOW_C_LEVELS flag in the Flask app — C1/C2 are excluded until ready to launch.
ACTIVE_LEVELS = ["a1", "a2", "b1", "b2"]


@router.get("/courses", response_model=list[CourseSummary])
def get_courses():
    """Return a summary list of all active courses."""
    t = TRANSLATIONS["en"]
    return [
        {
            "level":   t[f"{level}_level"],
            "title":   t[f"{level}_title"],
            "tagline": t[f"{level}_tagline"],
            "price":   t[f"{level}_price_desc"],
        }
        for level in ACTIVE_LEVELS
    ]


@router.get("/courses/{level}", response_model=CourseDetail)
def get_course(level: str):
    """Return full details for a single course by CEFR level (e.g. 'b1')."""
    level = level.lower()

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
