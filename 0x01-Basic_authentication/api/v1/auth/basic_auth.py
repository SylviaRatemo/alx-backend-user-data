#!/usr/bin/env python3
"""
class to perform basic authentication
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """Decode BAse4 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode_value = base64.b64decode(base64_authorization_header)
            return decode_value.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """Method to get user email and password from Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            email, pwd = decoded_base64_authorization_header.split(":")
            return email, pwd
