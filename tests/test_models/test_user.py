#!/usr/bin/python3
"""Defines a unittest for the user model"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Defines a class that contains the unittest cases for the User Model"""
    
    def test_user_instance(self):
        """test if user instance is created"""
        user1 = User()
        self.assertIsInstance(user1, User)

    def test_user_attributes(self):
        """test if user attributes are initializs correctly upon creation"""
        user1 = User(email="test@gmail.com", password="123455", first_name="Nick", last_name="Medo")
        self.assertEqual(user1.email, "test@gmail.com")
        self.assertEqual(user1.password, "123455")
        self.assertEqual(user1.first_name, "Nick")
        self.assertEqual(user1.last_name, "Medo")


if __name__ == '__main__':
    unittest.main()
