# English with Flor

A bilingual English/Spanish language school web application built with Python, Flask, and FastAPI. The platform handles student registration, course enrolment, and account management, with a companion REST API providing authenticated JSON access to the same data layer.

---

## Features

### Web application
- **Bilingual UI** — full English and Spanish support toggled via a `?lang=` URL parameter, applied consistently across all pages and form validation messages
- **Course catalogue** — individual pages for CEFR levels A1, A2, B1, and B2; C1 and C2 controlled by a feature flag for staged release
- **Authentication** — user registration and login with scrypt-hashed passwords via Werkzeug; session management via Flask-Login
- **Enrolment** — student type-aware form handling Argentine students (CUIT/CUIL, DNI with format validation) and international students (passport); collects a full postal address from all students
- **User dashboard** — view enrolment details; edit personal details, address, and password; delete account (GDPR-style data removal)
- **Admin dashboard** — role-protected view (`is_admin` flag) displaying all registered users, enrolments, and contact form submissions
- **Security** — CSRF protection on all forms; rate limiting on login, registration, and contact endpoints; `Content-Security-Policy`, `X-Frame-Options`, and `X-Content-Type-Options` headers; `SameSite=Lax` session cookies with `Secure` flag in production; generic error messages on registration to prevent account enumeration; duplicate enrolment guard
- **Contact form** — submissions persisted to the database; WhatsApp CTA for direct replies
- **Word of the Day** — daily-rotating vocabulary card driven by a date-based index against a curated word list; no additional database queries required
- **Feature flags** — boolean constants in `routes.py` control course visibility, enabling staged content releases without code changes

### REST API
- **JWT authentication** — HS256-signed tokens issued by `POST /auth/login`; verified on protected endpoints via a FastAPI dependency (`get_current_user`)
- **Pydantic validation** — all request bodies and response schemas are defined as Pydantic `BaseModel` subclasses; malformed requests return `422 Unprocessable Entity` automatically
- **Shared data layer** — connects to the same `school.db` SQLite database as the Flask app via a standalone SQLAlchemy session; no data duplication
- **CORS** — `CORSMiddleware` restricts browser cross-origin requests to permitted origins
- **Auto-generated documentation** — interactive Swagger UI available at `/docs`

---

## Tech stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Web framework | Flask 3 |
| Templates | Jinja2 |
| Database | SQLite via Flask-SQLAlchemy |
| Authentication | Flask-Login + Werkzeug |
| Forms | Flask-WTF |
| Rate limiting | Flask-Limiter |
| Production server | Gunicorn |
| Environment variables | python-dotenv |
| Front end | Custom CSS + vanilla JavaScript |
| REST API | FastAPI + Uvicorn |
| API authentication | python-jose (JWT / HS256) |
| API data validation | Pydantic v2 |

---

## Getting started

**1. Clone the repository**
```bash
git clone https://github.com/8m7nyv54n5-ux/english-with-flor.git
cd english-with-flor
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the project root. The application will not start without a secret key:
```
SECRET_KEY=your-secret-key-here
```

**5. Start the development server**
```bash
python3 run.py
```

The application is available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

> **macOS note:** Use `127.0.0.1` rather than `localhost`. On macOS, `localhost` may resolve to an IPv6 address, causing connection delays or failures with Flask's development server.

---

### Running the REST API

The FastAPI API runs as a separate process on port 8000:
```bash
uvicorn api.main:app --reload --port 8000
```

Interactive documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

#### Endpoints

| Method | Path | Auth | Description |
|---|---|---|---|
| `GET` | `/` | — | Health check |
| `GET` | `/word-of-the-day` | — | Today's vocabulary word; `?lang=es` returns a Spanish section label |
| `GET` | `/courses` | — | List of all active courses |
| `GET` | `/courses/{level}` | — | Full detail for a CEFR level (e.g. `/courses/b1`) |
| `POST` | `/auth/login` | — | Exchange credentials for a JWT access token |
| `POST` | `/enquiries` | JWT | Submit a prospective student enquiry |
| `GET` | `/users/me` | JWT | Retrieve the authenticated user's profile |
| `PUT` | `/users/me` | JWT | Update `first_name` and/or `last_name` |
| `DELETE` | `/users/me` | JWT | Permanently delete the authenticated user's account |

**Authentication:** call `POST /auth/login` with a valid `username` and `password`. Accounts are created via the web application. The response returns a JWT access token valid for 30 minutes; pass it on subsequent requests in the `Authorization: Bearer <token>` header.

---

### Production deployment

Use Gunicorn as the WSGI server in production:
```bash
gunicorn wsgi:app
```

The application is configured for deployment on PythonAnywhere (SQLite, persistent filesystem). Set `SESSION_COOKIE_SECURE=true` and `FLASK_DEBUG=false` as environment variables on the hosting platform.

---

## Project structure

```
english-with-flor/
├── run.py                  ← Development entry point
├── wsgi.py                 ← Production entry point (Gunicorn)
├── .env                    ← Environment variables (not committed)
├── requirements.txt
├── app/                    ← Flask web application
│   ├── __init__.py         ← Application factory, extensions
│   ├── models.py           ← SQLAlchemy models: User, Enrolment, ContactMessage
│   ├── routes.py           ← Main blueprint: public pages, feature flags
│   ├── auth.py             ← Auth blueprint: register, login, enrol, profile management, admin
│   ├── forms.py            ← WTForms form classes
│   ├── translations.py     ← EN/ES translation dictionary
│   ├── words.py            ← Word of the Day word list
│   ├── templates/          ← Jinja2 HTML templates
│   └── static/             ← CSS and images
└── api/                    ← FastAPI REST API
    ├── main.py             ← Application instance, CORS middleware, router registration
    ├── auth.py             ← JWT utilities and get_current_user dependency
    ├── database.py         ← SQLAlchemy engine, session factory, get_db dependency
    ├── models.py           ← Standalone SQLAlchemy User model (maps to Flask's schema)
    ├── schemas.py          ← Pydantic request and response models
    └── routes/
        ├── login.py        ← POST /auth/login
        ├── users.py        ← GET, PUT, DELETE /users/me
        ├── enquiries.py    ← POST /enquiries
        ├── courses.py      ← GET /courses, GET /courses/{level}
        └── words.py        ← GET /word-of-the-day
```

---

## Roadmap

- Password reset via email link (Flask-Mail + itsdangerous signed tokens)
- Booking flow for level test appointments
- Deployment to PythonAnywhere
