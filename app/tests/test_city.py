#!/usr/bin/env python3

import unittest
from datetime import datetime
from unittest.mock import MagicMock
from app.models.city import City
from app.models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.city = City(name="New York", country_id="US",
                         data_manager=self.mock_data_manager)

    def test_init(self):
        self.assertIsInstance(self.city, BaseModel)
        self.assertEqual(self.city.name, "New York")
        self.assertEqual(self.city.country_id, "US")
        self.assertIsNotNone(self.city.id)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_to_dict(self):
        self.city.id = "city_123"
        self.city.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.city.updated_at = datetime(2023, 6, 2, 12, 0, 0)
        city_dict = self.city.to_dict()
        expected_dict = {
            "city_id": "city_123",
            "city_name": "New York",
            "country_id": "US",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(city_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
