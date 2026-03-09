# api/routes/login.py
# POST /auth/login — authenticates a user and returns a signed JWT.

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
from api.schemas import Token
from api.auth import create_access_token
from api.database import get_db
from api.models import User
from api.limiter import limiter

router = APIRouter()


# 5 login attempts per minute per IP — protects against brute-force password attacks.
@limiter.limit("5/minute")
@router.post("/auth/login", response_model=Token)
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Validate credentials against school.db and return a JWT on success.

    Accepts form data (application/x-www-form-urlencoded) so Swagger's Authorize
    button works out of the box. A single generic 401 is returned for both bad
    username and bad password to prevent username enumeration.
    """
    user = db.query(User).filter(User.username == form_data.username).first()

    # werkzeug's check_password_hash matches the hashing used by the Flask app on registration.
    if not user or not check_password_hash(user.password_hash, form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
