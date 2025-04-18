"""
__init__.py – Application factory and global extension initialization.

This file sets up the Flask app instance, configures the database,
initializes the RESTful API interface, enables CORS, and registers blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

# Initialize extensions globally
db = SQLAlchemy()
api = Api()

def create_app():
    """
    Application factory function to create and configure the Flask app.
    Returns:
        app (Flask): The configured Flask app instance
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    api.init_app(app)
    CORS(app)

    # Register blueprints
    from .routes.cafes import cafes_bp
    app.register_blueprint(cafes_bp)

    return app
