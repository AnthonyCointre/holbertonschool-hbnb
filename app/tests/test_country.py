#!/usr/bin/env python3

import unittest
from datetime import datetime
from app.models.country import Country


class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country(name="United States", code="US")

    def test_init(self):
        self.assertIsInstance(self.country, Country)
        self.assertEqual(self.country.name, "United States")
        self.assertEqual(self.country.code, "US")
        self.assertIsNotNone(self.country.id)
        self.assertIsInstance(self.country.created_at, datetime)
        self.assertIsInstance(self.country.updated_at, datetime)

    def test_to_dict(self):
        self.country.id = "country_123"
        self.country.created_at = datetime(2023, 6, 1, 12, 0, 0)
        self.country.updated_at = datetime(2023, 6, 2, 12, 0, 0)

        country_dict = self.country.to_dict()

        expected_dict = {
            "country_id": "country_123",
            "name": "United States",
            "code": "US",
            "created_at": "2023-06-01T12:00:00",
            "updated_at": "2023-06-02T12:00:00"
        }

        self.assertEqual(country_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
