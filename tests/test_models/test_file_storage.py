#!/usr/bin/python3


from models.__init__ import storage
import unittest
from models.base_model import BaseModel
import os
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        from models.engine.file_storage import FileStorage
        self.storage = FileStorage()
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        self.storage.new(self.model1)
        self.storage.new(self.model2)
        all_objs = self.storage.all()
        self.assertIn(
                type(self.model1).__name__ + '.' + self.model1.id, all_objs)
        self.assertIn(
                type(self.model2).__name__ + '.' + self.model2.id, all_objs)

    def test_new(self):
        self.storage.new(self.model1)
        self.assertIn(
                type(
                    self.model1).__name__ + '.' + self.model1.id, self.storage.all())

    def test_save(self):
        self.storage.new(self.model1)
        self.storage.new(self.model2)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertIn(
                    type(self.model1).__name__ + '.' + self.model1.id, data)
            self.assertIn(
                    type(self.model2).__name__ + '.' + self.model2.id, data)

    def test_reload(self):
        self.storage.new(self.model1)
        self.storage.new(self.model2)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn
        (type(self.model1).__name__ + '.' + self.model1.id, all_objs)
        self.assertIn(
                type(self.model2).__name__ + '.' + self.model2.id, all_objs)
