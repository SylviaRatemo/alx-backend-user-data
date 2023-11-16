#!/usr/bin/env python3
"""DB Module
Implement the add_user method
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self.__session.add(new_user)
        self.__session.commit()
        return new_user
    
    def find_user_by(self, **kwargs) -> User:
        """FInd user based on filters
        """
        fields, values = [], []
        for k, v in kwargs.items():
            if hasattr(User, k):
                fields.append(getattr(User, k))
                values.append(v)
            else:
                raise InvalidRequestError()
        result = self.__session.query(User).filter(
            tuple_(*fields).in_([tuple(values)])
        ).first()
        if result is None:
            raise NoResultFound()
        return result

def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user at an id.
        """
        user = self.find_user_by(id=user_id)
        if user is None:
            return
        row = {}
        for k, v in kwargs.items():
            if hasattr(User, k):
                row[getattr(User, k)] = v
            else:
                raise ValueError()
        self.__session.query(User).filter(User.id == user_id).update(
            row,
            synchronize_session=False,
        )
        self.__session.commit()
