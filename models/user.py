#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Enum, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(BaseModel, UserMixin, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False)
    portfolio_url = Column(String(128), nullable=True)
    github_url = Column(String(128), nullable=True)
    role = Column(Enum('Employer', 'Job-Seeker'), nullable=False)
    email_verify = Column(Boolean, default=False)

    jobs = relationship('Job', back_populates='user', cascade='all, delete-orphan')
    applications = relationship('Application', back_populates='user', cascade='all, delete-orphan')
