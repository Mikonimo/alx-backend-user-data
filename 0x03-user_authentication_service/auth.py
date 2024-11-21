#!/usr/bin/env python3
"""Auth file"""
from bcrypt import hashpw, gensalt, checkpw


def _hash_password(password: str) -> bytes:
    """
    Encrypts a password
    Args:
        password (str): string arguments
    Returns:
        Bytes: salted hash of the input password
    """
    return hashpw(password.encode('utf-8'), gensalt())
