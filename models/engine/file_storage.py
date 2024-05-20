#!/usr/bin/python3
"""Defines class FileStorage"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """
    Defines class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_rep = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(dict_rep, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as file:
                dict_rep = json.load(file)
                classes = {
                        "BaseModel": BaseModel,
                        "User": User,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Place": Place,
                        "Review": Review
                        }
                for key, value in dict_rep.items():
                    class_name = key.split('.')[0]
                    if class_name in classes:
                        #Convert created_at and updated_at back to datetime
                        if 'created_at' in value and isinstance(value['created_at'], str):
                            value['created_at'] = datetime.fromisoformat(value['created_at'])
                        if 'updated_at' in value and isinstance(value['updated_at'], str):
                            value['updated_at'] = datetime.fromisoformat(value['updated_at'])


                        obj = classes[class_name](**value)
                        self.__objects[key] = obj

        except FileNotFoundError:
            pass
