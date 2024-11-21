#!/usr/bin/env python3
"""Auth file"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Encrypts a password
    Args:
        password (str): string arguments
    Returns:
        Bytes: salted hash of the input password
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database
    """

    def __init__(self):
        """DB Class Instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user
        Args:
            email (str): user's email
            password (str): user's password
        Returns:
            User: A new registered user."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
