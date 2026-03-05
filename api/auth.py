# api/auth.py
# JWT utility functions — token creation, verification, and the get_current_user dependency.

from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Extracts the Bearer token from the Authorization header on incoming requests.
# tokenUrl points to the login endpoint, which powers the "Authorize" button in /docs.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# In production, SECRET_KEY must be loaded from an environment variable.
# Any party that holds this key can forge valid tokens.
SECRET_KEY = "change-me-in-production"

# HS256 (HMAC-SHA256) — symmetric signing: the same key is used to sign and verify.
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


# ---------------------------------------------------------------------------
# create_access_token
# ---------------------------------------------------------------------------

def create_access_token(data: dict) -> str:
    """Sign and return a JWT containing the given claims plus an expiry timestamp."""
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload["exp"] = expire
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ---------------------------------------------------------------------------
# verify_token
# ---------------------------------------------------------------------------

def verify_token(token: str) -> str:
    """
    Decode and verify a JWT. Returns the username from the 'sub' claim if valid.

    Raises HTTP 401 for an invalid signature, expired token, or missing sub claim.
    A generic error message is returned in all cases to avoid leaking information.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception


# ---------------------------------------------------------------------------
# get_current_user  (FastAPI dependency)
# ---------------------------------------------------------------------------

def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """
    FastAPI dependency for protected routes — declare as Depends(get_current_user).

    oauth2_scheme extracts the raw token from the Authorization header before this
    function runs; if the header is absent FastAPI returns 401 automatically.
    Returns the authenticated username on success.
    """
    return verify_token(token)
