# api/database.py
# SQLAlchemy setup for the FastAPI app.
# Connects to the same school.db created by the Flask app — no data duplication.
# Sessions are managed manually via the get_db dependency rather than tied to a
# Flask app context.

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Resolve the absolute path to instance/school.db, one level above api/.
_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../instance/school.db"))
DATABASE_URL = f"sqlite:///{_db_path}"

# check_same_thread=False is required for SQLite when requests may be handled
# across multiple threads, as is the case with FastAPI.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    FastAPI dependency — yields a SQLAlchemy session for the duration of a request.

    The session is always closed in the finally block, even if the route raises
    an exception. Use as: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
