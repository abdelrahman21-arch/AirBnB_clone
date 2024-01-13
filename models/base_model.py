#!/usr/bin/python3
"""
BaseModel Module
"""

import models
import uuid
from datetime import datetime

tmf = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The Base Class"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, tmf))
                else:
                    setattr(self, key, value)
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """override srting function"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """update and save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary representaion of class"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].strftime(tmf)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(tmf)
        return new_dict
