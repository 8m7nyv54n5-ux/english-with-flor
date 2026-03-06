# api/tests/test_api.py
# pytest test suite for the English with Flor FastAPI.
#
# Run from the language_school/ directory with:
#   pytest api/tests/ -v


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

def test_root_returns_200(client):
    """GET / should return 200 and confirm the API is running."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "English with Flor API is running"}


# ---------------------------------------------------------------------------
# Word of the Day
# ---------------------------------------------------------------------------

def test_word_of_the_day_shape(client):
    """GET /word-of-the-day should return all expected fields."""
    response = client.get("/word-of-the-day")
    data = response.json()

    assert response.status_code == 200
    # Check every field the WordOfDay schema requires is present
    for field in ("label", "word", "phonetic", "part_of_speech", "definition", "example"):
        assert field in data, f"Missing field: {field}"


def test_word_of_the_day_english_label(client):
    """Default response (no lang param) should use the English label."""
    response = client.get("/word-of-the-day")

    assert response.json()["label"] == "Word of the Day"


def test_word_of_the_day_spanish_label(client):
    """?lang=es should return the Spanish label."""
    response = client.get("/word-of-the-day?lang=es")

    assert response.json()["label"] == "Palabra del día"


# ---------------------------------------------------------------------------
# Courses
# ---------------------------------------------------------------------------

def test_courses_list_returns_200(client):
    """GET /courses should return 200 and a non-empty list."""
    response = client.get("/courses")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_courses_list_item_shape(client):
    """Every item in GET /courses should have the required CourseSummary fields."""
    response = client.get("/courses")

    for course in response.json():
        for field in ("level", "title", "tagline", "price"):
            assert field in course, f"Missing field '{field}' in course: {course}"


def test_course_detail_valid_level(client):
    """GET /courses/a1 should return 200 and the full CourseDetail shape."""
    response = client.get("/courses/a1")
    data = response.json()

    assert response.status_code == 200
    for field in ("level", "title", "tagline", "price", "who_desc", "learn_items", "format_desc"):
        assert field in data, f"Missing field: {field}"


def test_course_detail_invalid_level_returns_404(client):
    """GET /courses/z9 should return 404 for an unrecognised course level."""
    response = client.get("/courses/z9")

    assert response.status_code == 404


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------

def test_login_valid_credentials_returns_token(client, test_user):
    """POST /auth/login with correct credentials should return a Bearer token."""
    response = client.post("/auth/login", json=test_user)
    data = response.json()

    assert response.status_code == 200
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password_returns_401(client, test_user):
    """POST /auth/login with a bad password should return 401."""
    response = client.post("/auth/login", json={
        "username": test_user["username"],
        "password": "wrongpassword",
    })

    assert response.status_code == 401


def test_login_unknown_user_returns_401(client):
    """POST /auth/login with a username that doesn't exist should return 401."""
    response = client.post("/auth/login", json={
        "username": "nobody",
        "password": "irrelevant",
    })

    assert response.status_code == 401


# ---------------------------------------------------------------------------
# Protected endpoints
# ---------------------------------------------------------------------------

def test_get_my_profile_with_valid_token(client, auth_token):
    """GET /users/me with a valid token should return the user's profile."""
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    data = response.json()

    assert response.status_code == 200
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"


def test_get_my_profile_without_token_returns_401(client):
    """GET /users/me with no token should return 401."""
    response = client.get("/users/me")

    assert response.status_code == 401


def test_get_my_profile_with_invalid_token_returns_401(client):
    """GET /users/me with a tampered token should return 401."""
    response = client.get(
        "/users/me",
        headers={"Authorization": "Bearer thisisnotavalidtoken"},
    )

    assert response.status_code == 401


# ---------------------------------------------------------------------------
# Enquiries
# ---------------------------------------------------------------------------

def test_post_enquiry_valid(client, auth_token):
    """POST /enquiries with a valid token and all required fields returns 201."""
    payload = {
        "name": "Lewis Nield",
        "email": "lewis@example.com",
        "message": "I'd like to know more about the B1 course.",
    }
    response = client.post(
        "/enquiries",
        json=payload,
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["message"] == payload["message"]
    assert "received_at" in data
    assert "confirmation" in data


def test_post_enquiry_missing_field_returns_422(client, auth_token):
    """POST /enquiries without a required field should return 422 (validation error)."""
    response = client.post(
        "/enquiries",
        json={"name": "Lewis Nield"},  # email and message are missing
        headers={"Authorization": f"Bearer {auth_token}"},
    )

    assert response.status_code == 422


def test_post_enquiry_no_token_returns_401(client):
    """POST /enquiries without a token should return 401."""
    response = client.post("/enquiries", json={
        "name": "Lewis Nield",
        "email": "lewis@example.com",
        "message": "Hello.",
    })

    assert response.status_code == 401
