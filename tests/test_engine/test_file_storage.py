#!/usr/bin/python3
"""Defines a unit test fot the filestorage module"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import os



class TestFileStorage(unittest.TestCase):
    """Defines a class that contains the unit test cases for the FileStorage"""
    def setup(self):
        """Automatically called for every single test we run"""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = 'test_file.json'
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists('test_file.json'):
            os.remove('test_file.jso')
        
    def test_save_and_reload(self):
        """
        test saving and reloading
        """
        obj = User()
        obj.save()
        self.assertTrue(os.path.exists('test_file.json'))
        self.storage.reload()
        key = f"User.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_new(self):
        obj = User()
        self.storage.new(obj)
        key = f"User.{obj.id}"
        self.assertIn(key, self.storage.all())

if __name__ == "__main__":
    unittest.main()

