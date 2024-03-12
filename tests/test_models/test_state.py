#!usr/bin/python3


import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, '')
