#!/usr/bin/env python3
"""Sets up a basic Flask app"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """
    GET /
    Returns:
        - JSON payload
    """
    return jsonify({"message": "Bienvenue"})
