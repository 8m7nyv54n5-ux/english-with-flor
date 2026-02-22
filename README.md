# English with Flor

A bilingual (English / Spanish) language school website built with Python and Flask.

Built as a Python learning project, working through Flask fundamentals step by step — routing, templates, databases, authentication, and security.

---

## Features

- Bilingual UI — full English and Spanish support via a `?lang=` URL toggle
- Course pages — Beginner (A1–A2), Intermediate (B1–B2), and Advanced (C1–C2)
- User registration and login with hashed passwords
- Course enrolment form — handles Argentine (CUIT/CUIL, DNI) and international (passport) students
- User dashboard showing enrolment details
- Login rate limiting to block brute-force attempts
- Patagonia photo slideshow on the home page
- Word of the Day — a daily-rotating English vocabulary card on the home page, selected from a curated list using a date-based index (no database required)
- Feature flags — course visibility controlled by simple boolean flags in `routes.py` (e.g. Advanced course toggled off until ready to launch)

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
| Environment variables | python-dotenv |
| Front end | Custom CSS |

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

**4. Create a `.env` file** in the project root with a secret key:
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

---

## Project structure

```
language_school/
├── run.py                  ← entry point
├── .env                    ← secret key (not committed)
├── requirements.txt
└── app/
    ├── __init__.py         ← app factory
    ├── models.py           ← User and Enrolment database models
    ├── routes.py           ← main blueprint (public pages)
    ├── auth.py             ← auth blueprint (register, login, enrol)
    ├── forms.py            ← WTForms form classes
    ├── translations.py     ← EN/ES text dictionary
    ├── words.py            ← curated word list for the Word of the Day feature
    ├── templates/          ← Jinja2 HTML templates
    └── static/             ← CSS and images
```

---

## Planned next steps

- Contact form
- Booking flow for level tests
- Admin view for the school to manage enrolments
- Deployment
