#!/usr/bin/env python3
"""Sets up a basic Flask app"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """
    GET /
    Returns:
        - JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    POST /users
        Registers new users
    Returns:
        - JSON payload"""
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    elif "password" not in form_data:
        return jsonify({"message": "password required"}), 400
    else:
        email = request.form.get("email")
        passwd = request.form.get("password")

        try:
            new_user = AUTH.register_user(email, passwd)
            return jsonify({
                "email": new_user.email,
                "message": "user created"
                })
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
