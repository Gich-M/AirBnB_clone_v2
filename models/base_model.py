#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instantiates a new model
        Args:
            args: A dictionary
            kwargs: Arguments for the constructor of the model
        Attributes:
            id: The unique identifier generated
            created_at: The date and time the instance was created
            updated_at: The date and time the instance was last updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(type(self).__name__, self.__id, self.__dict__)

    def __repr__(self):
        """Returns a string representation of the instance"""
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dicn = dict(self.__dict__)
        dicn["__class__"] = str(type(self).__name__)
        dicn["created_at"] = self.created_at.isoformat()
        dicn["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in dicn.keys():
            del dicn['_sa_instance_state']
        return dicn
    
    def delete(self):
        """Deletes instance from storage"""
        models.storage.delete(self)