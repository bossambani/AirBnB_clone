#!/usr/bin/python3
"""Defines the main class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
        Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initializes the required attributes for the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                        if isinstance(value, str):
                            value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel object

        Returns:
            str: A string containing the class name, id and dict
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance updated_at with the current date
        when the object is modified
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_rep = self.__dict__
        dict_rep['__class__'] = self.__class__.__name__
        if isinstance(dict_rep['created_at'], datetime):
            dict_rep['created_at'] = dict_rep['created_at'].isoformat()
        if isinstance(dict_rep['updated_at'], datetime):
            dict_rep['updated_at'] = dict_rep['updated_at'].isoformat()

        return dict_rep

if __name__ == "__main__":
    model = BaseModel()


