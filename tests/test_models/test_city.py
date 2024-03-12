#!/usr/bin/python3


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, '')
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, '')
