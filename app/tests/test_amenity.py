#!/usr/bin/env python3

import unittest
from datetime import datetime
from unittest.mock import MagicMock
from app.models.amenity import Amenity
from app.models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.amenity = Amenity(
            name="WiFi", data_manager=self.mock_data_manager)

    def test_init(self):
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertEqual(self.amenity.name, "WiFi")
        self.assertIsNotNone(self.amenity.id)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_to_dict(self):
        self.amenity.id = "amenity_123"
        self.amenity.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.amenity.updated_at = datetime(2023, 6, 2, 12, 0, 0)
        amenity_dict = self.amenity.to_dict()
        expected_dict = {
            "amenity_id": "amenity_123",
            "amenity_name": "WiFi",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(amenity_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
