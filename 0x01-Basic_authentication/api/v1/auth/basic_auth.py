#!/usr/bin/env python3
"""
class to perform basic authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class to handle basic authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """Extract the Base64 authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[len('Basic '):].strip()
