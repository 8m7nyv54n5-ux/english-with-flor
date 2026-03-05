# api/routes/users.py
# Profile endpoints for the authenticated user: GET, PUT, and DELETE /users/me.

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from api.auth import get_current_user
from api.database import get_db
from api.models import User
from api.schemas import UserProfile, UserUpdate

router = APIRouter()


@router.get("/users/me", response_model=UserProfile)
def get_my_profile(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return the profile of the currently authenticated user."""
    user = db.query(User).filter(User.username == current_user).first()

    # A 404 here means the account was deleted after the token was issued.
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.put("/users/me", response_model=UserProfile)
def update_my_profile(
    update: UserUpdate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update first_name and/or last_name for the currently authenticated user."""
    user = db.query(User).filter(User.username == current_user).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Only overwrite fields that were explicitly included in the request body.
    if update.first_name is not None:
        user.first_name = update.first_name
    if update.last_name is not None:
        user.last_name = update.last_name

    db.commit()
    db.refresh(user)  # re-read the row so the returned data reflects the committed state
    return user


@router.delete("/users/me", status_code=204)
def delete_my_account(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Permanently delete the authenticated user's account. Returns 204 No Content."""
    user = db.query(User).filter(User.username == current_user).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
