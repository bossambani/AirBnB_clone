#!/usr/bin/python3
"""Defines a unittest for the review model"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """defines the class"""
    def test_attribute(self):
        """Checks if the attributes are assigned correctly"""
        review1 = Review()
        self.assertEqual(review1.place_id, "")
        self.assertEqual(review1.user_id, "")
        self.assertEqual(review1.text, "")



if __name__ == "__main__":
    unittest.main()
