#!/usr/bin/python3
"""This module defines a class application"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Application(BaseModel, Base):
    """This class defines a application by various attributes"""
    __tablename__ = 'applications'
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    job_id = Column(String(60), ForeignKey("jobs.id"), nullable=False)
    cover_letter = Column(String(268), nullable=True)
    user = relationship('User', back_populates='applications')