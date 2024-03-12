#!/usr/bin/python3


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, '')
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, '')
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, '')
