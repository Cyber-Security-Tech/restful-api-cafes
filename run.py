"""
run.py – Entry point for the RESTful Café API app.

Initializes and runs the Flask application using the factory pattern.
"""

from app import create_app

# Create app instance
app = create_app()

if __name__ == '__main__':
    # Run in development mode
    app.run(debug=True, port=5000)
