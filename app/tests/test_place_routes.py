#!/usr/bin/env python3

import unittest
import json
from app.routes.place_routes import app

class TestPlaceRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def tearDown(self):
        pass

    def test_create_place(self):
        place_data = {
            'name': 'Test Place',
            'address': 'Test Address',
            'city_id': '1',
            'latitude': 0.0,
            'longitude': 0.0,
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'price_per_night': 100.0,
            'max_guests': 4,
            'amenity_ids': ['1', '2']
        }
        response = self.client.post('/places/', json=place_data)
        self.assertEqual(response.status_code, 201)
        new_place = json.loads(response.data.decode('utf-8'))
        self.assertEqual(new_place['name'], place_data['name'])

if __name__ == '__main__':
    unittest.main()
