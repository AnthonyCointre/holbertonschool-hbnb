#!/usr/bin/env python3

import unittest
from datetime import datetime
from unittest.mock import MagicMock
from app.models.user import User
from app.models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.user = User(
            email="test@gmail.com",
            first_name="John",
            last_name="Doe",
            data_manager=self.mock_data_manager
        )

    def test_init(self):
        self.assertIsInstance(self.user, BaseModel)
        self.assertEqual(self.user.email, "test@gmail.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertIsNotNone(self.user.id)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict(self):
        self.user.id = "user_123"
        self.user.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.user.updated_at = datetime(2023, 6, 2, 12, 0, 0)
        user_dict = self.user.to_dict()
        expected_dict = {
            "user_id": "user_123",
            "email": "test@gmail.com",
            "first_name": "John",
            "last_name": "Doe",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(user_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
