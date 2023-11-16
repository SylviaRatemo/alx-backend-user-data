#!/usr/bin/env python3
"""
SQLAlchemy model for db table users (mapping declaration)
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """The SQLAlchemy model
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hashed_password= Column(String, nullable=False)
    session_id = Column(String)
    reset_token = Column(String)