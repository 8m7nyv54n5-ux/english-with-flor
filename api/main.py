# api/main.py
# FastAPI application entry point.
# Run with: uvicorn api.main:app --reload --port 8000

from dotenv import load_dotenv
load_dotenv()  # loads .env before any module reads os.environ (e.g. api/auth.py)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import words, courses, enquiries, login, users
from api.models import Base
from api.database import engine

# Create any tables that don't yet exist in school.db (e.g. the new 'enquiry' table).
# Safe to run every startup — skips tables that already exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="English with Flor API")

# ---------------------------------------------------------------------------
# CORS middleware
# ---------------------------------------------------------------------------
# Restricts cross-origin browser requests to permitted origins only.
# allow_credentials must be True so the Authorization header is included.
# In production, replace allow_origins with the deployed front-end domain.
# Note: allow_origins=["*"] cannot be combined with allow_credentials=True.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5000",
        "http://localhost:5000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(words.router)
app.include_router(courses.router)
app.include_router(enquiries.router)
app.include_router(login.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "English with Flor API is running"}
