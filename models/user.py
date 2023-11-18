#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False)
    role = Column(Enum('Employer', 'Job-Seeker'), nullable=False)

    jobs = relationship('Job', back_populates='user', cascade='all, delete-orphan')
    applications = relationship('Application', back_populates='user', cascade='all, delete-orphan')
