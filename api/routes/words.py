# api/routes/words.py
# GET /word-of-the-day — reuses the WORDS list from the Flask app.

from fastapi import APIRouter, HTTPException
from api.schemas import WordOfDay
from datetime import date
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))
from app.words import WORDS
from app.translations import TRANSLATIONS

router = APIRouter()

SUPPORTED_LANGS = ["en", "es"]


@router.get("/word-of-the-day", response_model=WordOfDay)
def word_of_the_day(lang: str = "en"):
    """Return today's vocabulary word. Supports ?lang=es for a Spanish section label."""
    if lang not in SUPPORTED_LANGS:
        raise HTTPException(status_code=400, detail=f"Unsupported lang '{lang}'. Use 'en' or 'es'.")

    # Same date-based rotation used by the Flask home page.
    index = date.today().toordinal() % len(WORDS)
    word = WORDS[index]
    label = TRANSLATIONS[lang]["wotd_label"]

    return {**word, "label": label}
