# api/routes/words.py
# Handles the /word-of-the-day endpoint.
# Reuses the WORDS list from the Flask app — no duplication needed.

from fastapi import APIRouter, HTTPException
from api.schemas import WordOfDay
from datetime import date
import sys, os

# Add the project root to Python's path so we can import from app/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))
from app.words import WORDS
from app.translations import TRANSLATIONS

# Create a router — this is registered in main.py
router = APIRouter()

# Supported languages — used to validate the lang query param
SUPPORTED_LANGS = ["en", "es"]


# `lang` is a query parameter — it's not in the path, so FastAPI treats it as ?lang=
# `= "en"` makes it optional with a default value of "en"
@router.get("/word-of-the-day", response_model=WordOfDay)
def word_of_the_day(lang: str = "en"):
    """Return today's word. Use ?lang=es for Spanish labels."""
    # Validate the lang value — return 400 if unsupported
    if lang not in SUPPORTED_LANGS:
        raise HTTPException(status_code=400, detail=f"Unsupported lang '{lang}'. Use 'en' or 'es'.")

    # Same daily-rotation logic as the Flask app
    index = date.today().toordinal() % len(WORDS)
    word = WORDS[index]

    # Look up the label in the requested language
    label = TRANSLATIONS[lang]["wotd_label"]

    # Merge the label into the word dict and return
    return {**word, "label": label}
