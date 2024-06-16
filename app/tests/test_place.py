#!/usr/bin/env python3

import unittest
from datetime import datetime
from unittest.mock import MagicMock
from app.models.place import Place
from app.models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.place = Place(
            name="Test Place",
            description="A nice place to stay",
            address="123 Test St",
            city_id="city_123",
            latitude=37.7749,
            longitude=-122.4194,
            host_id="host_456",
            num_rooms=3,
            num_bathrooms=2,
            price_per_night=100,
            max_guests=4,
            amenity_ids=1,
            data_manager=self.mock_data_manager
        )

    def test_init(self):
        self.assertIsInstance(self.place, BaseModel)
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.description, "A nice place to stay")
        self.assertEqual(self.place.address, "123 Test St")
        self.assertEqual(self.place.city_id, "city_123")
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.host_id, "host_456")
        self.assertEqual(self.place.num_rooms, 3)
        self.assertEqual(self.place.num_bathrooms, 2)
        self.assertEqual(self.place.price_per_night, 100)
        self.assertEqual(self.place.max_guests, 4)
        self.assertEqual(self.place.amenity_ids, 1)
        self.assertIsNotNone(self.place.id)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_to_dict(self):
        self.place.id = "place_123"
        self.place.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.place.updated_at = datetime(2023, 6, 2, 12, 0, 0)
        place_dict = self.place.to_dict()
        expected_dict = {
            "place_id": "place_123",
            "place_name": "Test Place",
            "description": "A nice place to stay",
            "address": "123 Test St",
            "city_id": "city_123",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "host_id": "host_456",
            "num_rooms": 3,
            "num_bathrooms": 2,
            "price_per_night": 100,
            "max_guests": 4,
            "amenity_ids": 1,
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }
        self.assertEqual(place_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
