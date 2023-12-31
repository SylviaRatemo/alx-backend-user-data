#!/usr/bin/env python3
"""Authentication Module
hash passwords and returns bytes
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """Hash the passwords
    """
    encoded_password = password.encode('utf-8')
    result = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    return result


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Adds a new user to the database.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))