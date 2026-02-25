# wsgi.py
# Production entry point for Gunicorn.
# Unlike run.py, this file does NOT start a server — it just creates the Flask
# app object so Gunicorn can import it and serve it with multiple workers.
#
# Usage:  gunicorn wsgi:app
# That tells Gunicorn: "import the 'app' variable from the 'wsgi' module".

from app import create_app

# Create the Flask app — Gunicorn expects a module-level variable called 'app'
app = create_app()
