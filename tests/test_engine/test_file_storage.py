#!/usr/bin/python3
"""Defines a unit test fot the filestorage module"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel



class TestFileStorage(unittest.TestCase):
    """Defines a class that contains the unit test cases for the FileStorage"""
    def setup(self):
        """Automatically called for every single test we run"""
        self.storage = FileStorage()
        self.file_path = "file.json"

    def test_initialization(self):
        """
        checks if the FileStorage is initialized to file.json and the object
        to an empty dictionary
        """
        self.assertEqual(self.storage.__objects, {})
        self.assertEqual(self.storage.__file_path, "file.json")

if __name__ == "__main__":
    unittest.main()

