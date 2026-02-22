# run.py
# This is the entry point for the application.
# Run this file with: python3 run.py
# It imports the app factory from the app package and starts the Flask development server.

from app import create_app

# Create the Flask app using the factory function defined in app/__init__.py
app = create_app()

if __name__ == "__main__":
    # debug=True means the server restarts automatically when you save a file,
    # and shows helpful error pages. Never use debug=True in production.
    app.run(debug=True)
