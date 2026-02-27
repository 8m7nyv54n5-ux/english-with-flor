# api/main.py
# Entry point for the FastAPI app.
# Run with: uvicorn api.main:app --reload --port 8000

from fastapi import FastAPI
from api.routes import words, courses

# Create the FastAPI app instance — equivalent to Flask's app = Flask(__name__)
app = FastAPI(title="English with Flor API")

# Register routers — equivalent to Flask's app.register_blueprint()
app.include_router(words.router)
app.include_router(courses.router)


# @app.get("/") registers this function as a GET handler for the "/" path
# FastAPI automatically converts the returned dict to a JSON response
@app.get("/")
def root():
    return {"message": "English with Flor API is running"}
