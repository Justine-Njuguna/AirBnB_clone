# test_base_model.py

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        # Test creating an instance of BaseModel
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_str_representation(self):
        # Test __str__ method
        base_model = BaseModel()
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)
