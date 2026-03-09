# api/routes/enrolments.py
# GET /enrolments/me — returns the authenticated user's enrolment record.

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.schemas import EnrolmentOut
from api.auth import get_current_user
from api.database import get_db
from api.models import User, Enrolment

router = APIRouter()


@router.get("/enrolments/me", response_model=EnrolmentOut)
def get_my_enrolment(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Return the enrolment record for the currently authenticated user.

    get_current_user extracts the username from the JWT and returns 401 if
    the token is absent or invalid. A 404 is returned if the user has not
    yet enrolled on a course.
    """
    # Look up the user row so we have their id.
    user = db.query(User).filter(User.username == current_user).first()

    # Query the enrolment table for a row belonging to this user.
    enrolment = db.query(Enrolment).filter(Enrolment.user_id == user.id).first()

    if not enrolment:
        raise HTTPException(status_code=404, detail="No enrolment found for this user")

    return enrolment
