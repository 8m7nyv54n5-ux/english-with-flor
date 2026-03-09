# api/tests/conftest.py
# Pytest configuration and shared fixtures.
#
# conftest.py is a special file pytest loads automatically before any tests run.
# Fixtures defined here are available to every test file in this directory
# without needing to import them.

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from werkzeug.security import generate_password_hash

from api.main import app
from api.database import get_db
from api.models import Base, Enrolment, User


# ---------------------------------------------------------------------------
# Test database
# ---------------------------------------------------------------------------
# We use an in-memory SQLite database so tests never touch the real school.db.
# "?check_same_thread=False" is required for SQLite when used with FastAPI's
# threading model (same as the production database.py).
TEST_DATABASE_URL = "sqlite:///:memory:"

test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    # StaticPool forces all sessions to share the same connection.
    # Without this, each new session gets its own empty in-memory database,
    # so tables created by create_all() are invisible to request sessions.
    poolclass=StaticPool,
)

# Create all tables defined in api/models.py inside the in-memory database.
# This runs once when conftest.py is first loaded.
Base.metadata.create_all(bind=test_engine)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    """
    A replacement for the real get_db dependency.
    Yields a session connected to the in-memory test database instead of school.db.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def client():
    """
    Yields a FastAPI TestClient with the database dependency swapped out.

    app.dependency_overrides is a dict that tells FastAPI: "whenever a route
    asks for get_db, call override_get_db instead." This is FastAPI's built-in
    mechanism for replacing dependencies in tests — no monkey-patching needed.

    The override is cleared after each test so tests stay independent.
    """
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture()
def test_user(client):
    """
    Creates a user in the test database and returns their credentials as a dict.

    We use werkzeug's generate_password_hash so the stored hash matches what
    the login route expects (it calls check_password_hash from the same library).

    The user is inserted directly via SQLAlchemy rather than through the API,
    because there is no POST /users registration endpoint — we just need a
    known user to exist so login tests have something to authenticate against.
    """
    db = TestingSessionLocal()
    user = User(
        username="testuser",
        email="test@example.com",
        first_name="Test",
        last_name="User",
        password_hash=generate_password_hash("testpassword"),
        is_admin=False,
    )
    db.add(user)
    db.commit()
    db.close()

    # Yield the plain-text credentials so tests can POST them to /auth/login
    yield {"username": "testuser", "password": "testpassword"}

    # Clean up: remove the user after the test so the next test starts fresh
    db = TestingSessionLocal()
    db.query(User).filter(User.username == "testuser").delete()
    db.commit()
    db.close()


@pytest.fixture()
def enrolled_user(client, test_user):
    """
    Extends test_user by also seeding an Enrolment row for that user.

    Builds on fixture chaining — test_user creates the User, this fixture
    then looks up that user's id to attach a matching Enrolment record.
    Returns the same credentials dict so the test can still log in normally.
    """
    db = TestingSessionLocal()
    user = db.query(User).filter(User.username == "testuser").first()
    # Store the id as a plain int now — once the session closes, accessing
    # user.id via the ORM object raises DetachedInstanceError.
    user_id = user.id
    enrolment = Enrolment(
        user_id=user_id,
        user_type="argentina",
        course="B1 — Getting There",
        cuit_cuil="20-12345678-9",
        dni="12345678",
        passport_no=None,
        address_line="Av. Corrientes 1234",
        city="Buenos Aires",
        province="CABA",
        country="Argentina",
        postcode="C1043",
    )
    db.add(enrolment)
    db.commit()
    db.close()

    yield test_user

    # Clean up the enrolment row after the test
    db = TestingSessionLocal()
    db.query(Enrolment).filter(Enrolment.user_id == user_id).delete()
    db.commit()
    db.close()


@pytest.fixture()
def auth_token(client, test_user):
    """
    Logs in as the test user and returns the Bearer token string.

    Fixtures can depend on other fixtures — pytest wires them up automatically.
    Any test that needs an authenticated client can use this fixture directly.
    """
    # Login uses form data (OAuth2PasswordRequestForm), not JSON — use data= not json=
    response = client.post("/auth/login", data=test_user)
    return response.json()["access_token"]
