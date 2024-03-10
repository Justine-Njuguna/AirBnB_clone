# test_base_model.py

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_create_instance_from_dict(self):
        # Create a dictionary representation
        base_model_dict = {
            '__class__': 'BaseModel',
            'id': '123',
            'created_at': '2023-05-01T12:34:56.789012',
            'updated_at': '2023-05-02T10:20:30.123456'
        }

        # Recreate instance from dictionary
        recreated_instance = BaseModel(**base_model_dict)

        # Check attributes
        self.assertEqual(
                recreated_instance.id, '123')
        self.assertEqual(
                recreated_instance.created_at,
                datetime(2023, 5, 1, 12, 34, 56, 789012))
        self.assertEqual(
                recreated_instance.updated_at,
                datetime(2023, 5, 2, 10, 20, 30, 123456))

    def test_create_new_instance(self):
        # Create a new instance
        base_model_instance = BaseModel()

        # Check attributes
        self.assertIsInstance(base_model_instance.id, str)
        self.assertIsInstance(base_model_instance.created_at, datetime)
        self.assertIsInstance(base_model_instance.updated_at, datetime)
