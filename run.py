# run.py
# This is the entry point for the application.
# Run this file with: python3 run.py
# It imports the app factory from the app package and starts the Flask development server.

from app import create_app

# Create the Flask app using the factory function defined in app/__init__.py
app = create_app()

if __name__ == "__main__":
    # FLASK_DEBUG is read from .env — set to True for development, False (or omit) for production.
    # When True the server restarts automatically when you save a file,
    # and shows helpful error pages in the browser.
    import os
    debug = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug)
