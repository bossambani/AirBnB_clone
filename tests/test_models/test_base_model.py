#!/usr/bin/python3i
"""Defines a unittest for the basemodel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Defines a class that contains the unittest cases for the BaseModel"""
    def setUp(self):
        """Automatically called for every single test we run"""
        self.my_model = BaseModel()

    def test_default_initilization(self):
        """
        checks if the attributes are instances of the initialized type
        and if the created_at and updated_at are equal
        """
        self.assertTrue(isinstance(self.my_model.id, str))
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_kwargs_instance_representation(self):
        """
        checks if the kwargs implementation converts back the values stored to
        the initial state of the data
        """

        my_data = {
            'id': '1234567334343498',
            'created_at': '2024-05-16T19:47:49.727335',
            'updated_at': '2024-05-16T19:47:49.727335'
            }
        my_model1 = BaseModel(**my_data)
        self.assertEqual(my_model1.id, '1234567334343498')
        self.assertEqual(
                my_model1.created_at,
                datetime.fromisoformat('2024-05-16T19:47:49.727335')
                )
        self.assertEqual(
                my_model1.updated_at,
                datetime.fromisoformat('2024-05-16T19:47:49.727335')
                )

    def test_save_updates_updated_at(self):
        """Defies a test method which checks if the updated_at attribute
        is successfully updated"""
        self.my_model.save()

        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_to_dict(self):
        """
        verify that the dictionary contains all attributes of the instance,
        Check that the `'__class__'` key is present and has the corect value,
        Ensures that the datetime attributes(`created_at` and `updated_at`)
        are formatted correctly in ISO format
        """

        # convert BaseModel instance to dictionary
        dict_rep = self.my_model.to_dict()

        # checks that all the attributes are present in the dictionary
        self.assertIn('id', dict_rep)
        self.assertIn('created_at', dict_rep)
        self.assertIn('updated_at', dict_rep)

        # checks that '__class__' key has the correct value
        self.assertEqual(dict_rep['__class__'], 'BaseModel')

        # checks that datetime attribute are formatted correctly
        self.assertTrue(isinstance(dict_rep['created_at'], str))
        self.assertTrue(isinstance(dict_rep['updated_at'], str))

    def test__str__(self):
        """
        Testing if the sting representation contains the class name,
        id attributes
        """
        output = str(self.my_model)
        expected_output = (
                f"[BaseModel] ({self.my_model.id}) {self.my_model.__dict__}"
                )
        self.assertEqual(output, expected_output)

    def test_valid_id_UUID(self):
        """
        verifies that the 'id' attribute of the `BaseModel` instance
        is a valid UUID
        """
        self.assertTrue(uuid.UUID(self.my_model.id))

    def test_created_at_and_updated_at_have_different_values(self):
        """
        Tesets if the created_at attribute and updated_at attributes
        are different
        """
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_created_at_and_updated_at_are_instance_of_datetime(self):
        """
        checks if the created_at and updated_at attributes are instance of
        datetime
        """
        self.assertTrue(isinstance(self.my_model.created_at, datetime))
        self.assertTrue(isinstance(self.my_model.created_at, datetime))

    def test_id_uniqueness(self):
        """
        creates several instances of the model to check if the id is unique
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_attribute_access(self):
        """
        verifies that all attributes can directly be accessed
        """
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
