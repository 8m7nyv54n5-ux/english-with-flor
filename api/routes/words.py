# api/routes/words.py
# Handles the /word-of-the-day endpoint.
# Reuses the WORDS list from the Flask app — no duplication needed.

from fastapi import APIRouter
from datetime import date
import sys, os

# Add the project root to Python's path so we can import from app/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))
from app.words import WORDS

# Create a router — this is registered in main.py
router = APIRouter()


@router.get("/word-of-the-day")
def word_of_the_day():
    # Same daily-rotation logic as the Flask app
    index = date.today().toordinal() % len(WORDS)
    return WORDS[index]
