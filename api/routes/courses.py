# api/routes/courses.py
# Handles course-related endpoints.

from fastapi import APIRouter
from api.schemas import CourseSummary
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
