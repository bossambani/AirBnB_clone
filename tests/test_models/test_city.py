#!/usr/bin/python3
"""Defines a unittest for the city model"""
import unittest
from models.city import City


class TestState(unittest.TestCase):
    """defines class TestState"""
    def test_attributes(self):
        city1 = City()
        self.assertEqual(city1.state_id, "")
        self.assertEqual(city1.name, "")

if __name__ == "__main__":
    unittest.main()

