# api/routes/login.py
# POST /auth/login — authenticates a user and returns a signed JWT.

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
from api.schemas import LoginRequest, Token
from api.auth import create_access_token
from api.database import get_db
from api.models import User

router = APIRouter()


@router.post("/auth/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Validate credentials against school.db and return a JWT on success.

    A single generic 401 is returned for both bad username and bad password
    to prevent username enumeration.
    """
    user = db.query(User).filter(User.username == request.username).first()

    # werkzeug's check_password_hash matches the hashing used by the Flask app on registration.
    if not user or not check_password_hash(user.password_hash, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
