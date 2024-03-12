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
        self.storage = FileStorage()
        self.base_model1 = BaseModel()
        self.base_model2 = BaseModel()
        self.user1 = User(email="user1@example.com", password="password1")
        self.state1 = State(name="California")
        self.city1 = City(state_id=self.state1.id, name="Los Angeles")
        self.amenity1 = Amenity(name="Wifi")
        self.place1 = Place(city_id=self.city1.id, user_id=self.user1.id,
                            name="Cozy Apartment", description="A cozy place to stay",
                            number_rooms=2, number_bathrooms=1, max_guest=4,
                            price_by_night=100, latitude=34.0522, longitude=-118.2437)
        self.review1 = Review(place_id=self.place1.id, user_id=self.user1.id,
                              text="Great experience, highly recommended!")

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        self.storage.new(self.base_model1)
        self.storage.new(self.user1)
        self.storage.new(self.state1)
        self.storage.new(self.city1)
        self.storage.new(self.amenity1)
        self.storage.new(self.place1)
        self.storage.new(self.review1)
        all_objs = self.storage.all()
        self.assertIn(
            type(self.base_model1).__name__ + '.' + self.base_model1.id, all_objs)
        self.assertIn(
            type(self.user1).__name__ + '.' + self.user1.id, all_objs)
        self.assertIn(
            type(self.state1).__name__ + '.' + self.state1.id, all_objs)
        self.assertIn(
            type(self.city1).__name__ + '.' + self.city1.id, all_objs)
        self.assertIn(
            type(self.amenity1).__name__ + '.' + self.amenity1.id, all_objs)
        self.assertIn(
            type(self.place1).__name__ + '.' + self.place1.id, all_objs)
        self.assertIn(
            type(self.review1).__name__ + '.' + self.review1.id, all_objs)

    def test_new(self):
        self.storage.new(self.base_model1)
        self.assertIn(
            type(self.base_model1).__name__ + '.' + self.base_model1.id, self.storage.all())

    def test_save(self):
        self.storage.new(self.base_model1)
        self.storage.new(self.user1)
        self.storage.new(self.state1)
        self.storage.new(self.city1)
        self.storage.new(self.amenity1)
        self.storage.new(self.place1)
        self.storage.new(self.review1)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertIn(
                type(self.base_model1).__name__ + '.' + self.base_model1.id, data)
            self.assertIn(
                type(self.user1).__name__ + '.' + self.user1.id, data)
            self.assertIn(
                type(self.state1).__name__ + '.' + self.state1.id, data)
            self.assertIn(
                type(self.city1).__name__ + '.' + self.city1.id, data)
            self.assertIn(
                type(self.amenity1).__name__ + '.' + self.amenity1.id, data)
            self.assertIn(
                type(self.place1).__name__ + '.' + self.place1.id, data)
            self.assertIn(
                type(self.review1).__name__ + '.' + self.review1.id, data)

    def test_reload(self):
        self.storage.new(self.base_model1)
        self.storage.new(self.user1)
        self.storage.new(self.state1)
        self.storage.new(self.city1)
        self.storage.new(self.amenity1)
        self.storage.new(self.place1)
        self.storage.new(self.review1)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn(
            type(self.base_model1).__name__ + '.' + self.base_model1.id, all_objs)
        self.assertIn(
            type(self.user1).__name__ + '.' + self.user1.id, all_objs)
        self.assertIn(
            type(self.state1).__name__ + '.' + self.state1.id, all_objs)
        self.assertIn(
            type(self.city1).__name__ + '.' + self.city1.id, all_objs)
        self.assertIn(
            type(self.amenity1).__name__ + '.' + self.amenity1.id, all_objs)
        self.assertIn(
            type(self.place1).__name__ + '.' + self.place1.id, all_objs)
        self.assertIn(
            type(self.review1).__name__ + '.' + self.review1.id, all_objs)
