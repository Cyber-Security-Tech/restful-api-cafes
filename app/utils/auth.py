"""
auth.py – Handles simple API key-based authentication for protected routes.
"""

import os
from dotenv import load_dotenv
from flask import request

# Load environment variables
load_dotenv()

# Fetch API key from environment variable
API_KEY = os.getenv("API_KEY")

def is_authorized(request):
    """
    Check if the incoming request includes the correct API key.
    Args:
        request (flask.Request): The incoming HTTP request
    Returns:
        bool: True if authorized, False otherwise
    """
    user_key = request.headers.get("x-api-key")
    return user_key == API_KEY
