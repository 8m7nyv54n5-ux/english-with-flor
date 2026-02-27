# English with Flor

A bilingual (English / Spanish) language school website built with Python and Flask.

Built as a Python learning project, working through Flask fundamentals step by step — routing, templates, databases, authentication, and security — with a companion FastAPI REST API built alongside as a Step 6 learning project.

---

## Features

- Bilingual UI — full English and Spanish support via a `?lang=` URL toggle
- Course pages — individual CEFR levels: A1, A2, B1, B2 (live), C1 and C2 (coming soon)
- User registration and login with hashed passwords (scrypt)
- Course enrolment form — handles Argentine (CUIT/CUIL, DNI) and international (passport) students, with format validation on identity fields; collects a full address (street, city, province, country, postcode) from all students regardless of type
- User dashboard showing enrolment details, with the ability to edit personal details, address, and password, and delete account; admin users see a direct link to the admin dashboard
- Admin dashboard — password-protected view for the school owner showing all registered students, enrolments, and contact messages
- Security hardening — rate limiting on login, registration, and contact form; CSRF protection on all forms; security headers (X-Content-Type-Options, X-Frame-Options, Content-Security-Policy); POST-only logout; session cookies set to SameSite=Lax and Secure in production; generic registration error prevents account enumeration; duplicate enrolment guard prevents data integrity issues
- Patagonia photo slideshow on the home page — auto-advances every 4.5 seconds with manual controls
- Student testimonials — cycling carousel of real student quotes, auto-advancing every 8 seconds with a CSS fade transition
- Word of the Day — a daily-rotating English vocabulary card on the home page, selected from a curated list using a date-based index (no database required)
- Contact form — messages saved to the database with a WhatsApp CTA for quick replies
- Custom error pages — styled 404 and 500 pages with bilingual support
- Feature flags — course visibility controlled by simple boolean flags in `routes.py` (e.g. `SHOW_C_LEVELS` toggles C1 and C2 courses on when ready to launch)

---

## Tech stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Web framework | Flask 3 |
| Templates | Jinja2 |
| Database | SQLite via Flask-SQLAlchemy |
| Authentication | Flask-Login + Werkzeug password hashing |
| Forms | Flask-WTF |
| Rate limiting | Flask-Limiter |
| Production server | Gunicorn |
| Environment variables | python-dotenv |
| Front end | Custom CSS + vanilla JavaScript |
| REST API | FastAPI + Uvicorn |

---

## Running locally

**1. Clone the repo**
```
git clone https://github.com/8m7nyv54n5-ux/english-with-flor.git
cd english-with-flor
```

**2. Create and activate a virtual environment**
```
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```
pip install -r requirements.txt
```

**4. Create a `.env` file** in the project root with a secret key (the app will refuse to start without this):
```
SECRET_KEY=your-secret-key-here
```

**5. Run the app**
```
python3 run.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

> **Note for macOS users:** Use `127.0.0.1:5000` rather than `localhost:5000`. On newer versions of macOS, `localhost` can resolve slowly or fail due to IPv6 handling.

To stop the server press `Ctrl+C` in your terminal. If the port gets stuck in use, run:
```
kill $(lsof -ti:5000)
```

### Running the REST API

The FastAPI API runs as a separate server on port 8000:
```
uvicorn api.main:app --reload --port 8000
```

Then open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the auto-generated interactive documentation.

Available endpoints:
- `GET /` — health check
- `GET /word-of-the-day` — today's vocabulary word
- `GET /courses` — list of all active courses
- `GET /courses/{level}` — detail for a specific CEFR level (e.g. `/courses/b1`)

---

### Running in production

For production, use Gunicorn instead of Flask's built-in server:
```
gunicorn wsgi:app
```

This serves the app with multiple workers for better performance and reliability. Hosting platforms like Render or Railway will use this command as their start command.

---

## Project structure

```
language_school/
├── run.py                  ← Flask development entry point
├── wsgi.py                 ← Flask production entry point (Gunicorn)
├── .env                    ← secret key (not committed)
├── requirements.txt
├── app/                    ← Flask web app
│   ├── __init__.py         ← app factory
│   ├── models.py           ← User, Enrolment, and ContactMessage database models
│   ├── routes.py           ← main blueprint (public pages)
│   ├── auth.py             ← auth blueprint (register, login, enrol, edit profile, change password, delete account, admin)
│   ├── forms.py            ← WTForms form classes
│   ├── translations.py     ← EN/ES text dictionary
│   ├── words.py            ← curated word list for the Word of the Day feature
│   ├── templates/          ← Jinja2 HTML templates
│   └── static/             ← CSS and images
└── api/                    ← FastAPI REST API
    ├── main.py             ← API entry point
    ├── schemas.py          ← Pydantic response models
    └── routes/
        ├── words.py        ← GET /word-of-the-day
        └── courses.py      ← GET /courses, GET /courses/{level}
```

---

## Planned next steps

- Password reset via email link
- Booking flow for level tests — WhatsApp CTA added (placeholder number, swap in real number when ready)
- FastAPI — POST /contact endpoint, JWT authentication
- Deployment
