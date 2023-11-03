#!/usr/bin/python3
"""
Contains class BaseModel where future models will be derived
"""
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid


Base = declarative_base()


class BaseModel():
    """BaseModel class from which future classes will be derived"""
    #Base Model columns
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize instance variables"""
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        val = datetime.fromisoformat(val)
                    setattr(self, key, val)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of class"""
        cls = self.__class__.__name__
        return ("[{}] ({}) {}".format(cls, self.id, self.__dict__))
    
    def save(self):
        """Updates the updated_at attribute to current time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()