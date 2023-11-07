#!/usr/bin/env python3
"""
class to manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
     class to manage the API authentication.
     methods: require_auth
              authorization_header
              current_user
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Dummy implementation for require_auth.
        Returns False for now.

        Args:
            path (str): The path to check for authentication.
            excluded_paths (List[str]): List of paths to exclude

        Returns:
            bool: Always returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Dummy implementation for authorization_header.
        Returns None for now.

        Args:
            request: The Flask request object.

        Returns:
            str: Always returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Dummy implementation for current_user.
        Returns None for now.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar('User'): Always returns None.
        """
        return None
