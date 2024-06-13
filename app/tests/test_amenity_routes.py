#!/usr/bin/env python3

import unittest
from datetime import datetime
from flask import Flask
from flask.testing import FlaskClient
from flask_restx import Api, fields, Namespace
from app.routes.amenity_routes import app, amenities_db, next_id, AmenityList, AmenityDetail

class TestAmenityRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Reset amenities_db and next_id before each test
        global amenities_db
        global next_id
        amenities_db = [
            {'id': 1, 'name': 'Wifi', 'created_at': datetime.now(), 'updated_at': datetime.now()},
            {'id': 2, 'name': 'Parking', 'created_at': datetime.now(), 'updated_at': datetime.now()}
        ]
        next_id = 3

    def tearDown(self):
        pass

    def test_get_all_amenities(self):
        response = self.app.get('/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(amenities_db))

    def test_get_specific_amenity(self):
        amenity_id = 1
        response = self.app.get(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], amenity_id)

    def test_create_new_amenity(self):
        new_amenity_data = {
            'name': 'Gym'
        }
        response = self.app.post('/amenities/', json=new_amenity_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_update_amenity(self):
        amenity_id = 1
        updated_amenity_data = {
            'name': 'Updated Wifi'
        }
        response = self.app.put(f'/amenities/{amenity_id}', json=updated_amenity_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], updated_amenity_data['name'])

    def test_delete_amenity(self):
        amenity_id = 2
        response = self.app.delete(f'/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
