#!/usr/bin/python3
"""This module defines a class Job"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship


class Job(BaseModel, Base):
    """This class defines a job by various attributes"""
    __tablename__ = 'jobs'
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    title = Column(String(128), nullable=True)
    description = Column(String(128), nullable=True)
    location = Column(String(128), nullable=False)
    salary = Column(String(128), nullable=False)
    requirements = Column(String(128), nullable=False)
    deadline = Column(DateTime, nullable=False, default=datetime.utcnow)
    user = relationship('User', back_populates='jobs')