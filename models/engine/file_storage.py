#!/usr/bin/python3
"""Defines class FileStorage"""
import json
import os
from models.base_model import BaseModel


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
                        }
                for key, value in dict_rep.items():
                    class_name = key.split('.')[0]
                    if class_name in classes:
                        obj = classes[class_name](**value)
                        self.__objects[key] = obj

        except FileNotFoundError:
            pass
