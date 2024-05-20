#!/usr/bin/python3
"""Defines a unittest for the place model"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """defines the class"""
    def test_attribute(self):
        """Checks if the attributes are assigned correctly"""
        place1 = Place()
        self.assertEqual(place1.city_id, "")
        self.assertEqual(place1.user_id, "")
        self.assertEqual(place1.name, "")
        self.assertEqual(place1.description, "")
        self.assertEqual(place1.number_rooms, 0)
        self.assertEqual(place1.number_bathrooms, 0)
        self.assertEqual(place1.max_guest, 0)
        self.assertEqual(place1.price_by_night, 0)
        self.assertEqual(place1.latitude, 0.0)
        self.assertEqual(place1.longitude, 0.0)
        self.assertEqual(place1.amenity_ids, [])

if __name__ == "__main__":
    unittest.main()
