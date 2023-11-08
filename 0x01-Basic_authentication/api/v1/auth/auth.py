#!/usr/bin/env python3
"""
class to manage the API authentication.
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """
     class to manage the API authentication.
     methods: require_auth
              authorization_header
              current_user
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Implementation for require_auth.
        Args:
            path (str): The path to check for authentication.
            excluded_paths (List[str]): List of paths to exclude

        Returns:
            bool: Always returns False.
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) < 1:
            return True
        path = path.rstrip('/') + '/'
        excluded_paths = [p.rstrip('/') + '/' for p in excluded_paths]

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        implementation for authorization_header.
        Args:
            request: The Flask request object.

        Returns:
            str: Always returns None.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

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
