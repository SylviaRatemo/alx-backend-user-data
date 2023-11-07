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
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[len('Basic '):].strip()
