#!/usr/bin/python3

import unittest
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_default_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_specified_values(self):
        user = User(
                email="test@example.com",
                password="password123",
                first_name="John",
                last_name="Doe"
                )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_set_get_email(self):
        self.user.email = "test@example.com"
        self.assertEqual(self.user.email, "test@example.com")

    def test_set_get_password(self):
        self.user.password = "password123"
        self.assertEqual(self.user.password, "password123")

    def test_set_get_first_name(self):
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")

    def test_set_get_last_name(self):
        self.user.last_name = "Doe"
        self.assertEqual(self.user.last_name, "Doe")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            self.user.email = "invalid_email"

    def test_invalid_password(self):
        with self.assertRaises(ValueError):
            self.user.password = ""

    def test_invalid_first_name(self):
        with self.assertRaises(ValueError):
            self.user.first_name = ""

    def test_invalid_last_name(self):
        with self.assertRaises(ValueError):
            self.user.last_name = ""

    def test_save_reload(self):
        user = User(
                email="test@example.com",
                password="password123",
                first_name="John",
                last_name="Doe"
                )
        FileStorage().new(user)
        FileStorage().save()
        FileStorage().reload()
        loaded_user = FileStorage().all()["User." + user.id]
        self.assertEqual(user.email, loaded_user.email)
        self.assertEqual(user.password, loaded_user.password)
        self.assertEqual(user.first_name, loaded_user.first_name)
        self.assertEqual(user.last_name, loaded_user.last_name)
