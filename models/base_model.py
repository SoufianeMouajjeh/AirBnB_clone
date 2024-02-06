#!/usr/bin/python3
"""
a class define all common attributes/methods for other classes

"""
from datetime import datetime
import uuid


class BaseModel:
    """ define attributes && kwargs"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time)
                else:
                    self.__dict__[value] = value

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """return the dictionary of the basemodel instance"""
        dict = self.__dict__.copy()
        dict['__class__'] = type(self).__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
