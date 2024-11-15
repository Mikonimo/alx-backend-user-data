#!/usr/bin/env python3
"""This module contains the class Auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method that returns False - path and excluded paths"""
        return False

    def authorization_header(self, request=None) -> str:
        """Public method that returns None - request will
        be the Flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'): # type: ignore
        """Public that retuns None - request will be the
        Flask request object"""
        return None
