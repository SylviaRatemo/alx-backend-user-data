#!/usr/bin/env python3
"""
class to manage the session authentication.
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """class to manage session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create session ID for the user
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns User ID based on Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id
