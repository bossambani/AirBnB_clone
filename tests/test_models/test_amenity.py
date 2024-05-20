#!/usr/bin/python3
"""Defines a unittest for the amenity model"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """defines the class"""
    def test_attribute(self):
        """Checks if the attribute is assigned to an empty string"""
        amenity1 = Amenity()
        self.assertEqual(amenity1.name, "")

if __name__ == "__main__":
    unittest.main()
