#!/usr/bin/env python3

import unittest
from flask import Flask
from flask_restful import Api
from app.models.city import City, CityCollection
from app.routes.city_routes import cityCollectionResource, cityResource

class CityRoutesTestCase(unittest.TestCase):
    def setUp(self):
        """Create a test client and initialize necessary variables."""
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(cityCollectionResource, '/cities')
        self.api.add_resource(cityResource, '/cities/<string:city_id>')
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_add_city(self):
        """Test adding a new city."""
        response = self.client.post('/cities', json={
            "id": "1",
            "name": "Paris",
            "country_code": "FR"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('City added successfully', response.get_json()['message'])

    def test_get_all_cities(self):
        """Test retrieving all cities."""
        self.client.post('/cities', json={"id": "1", "name": "Paris", "country_code": "FR"})
        response = self.client.get('/cities')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_get_city_by_id(self):
        """Test retrieving a city by ID."""
        self.client.post('/cities', json={"id": "1", "name": "Paris", "country_code": "FR"})
        response = self.client.get('/cities/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], "Paris")

    def test_update_city(self):
        """Test updating a city's name."""
        self.client.post('/cities', json={"id": "1", "name": "Paris", "country_code": "FR"})
        response = self.client.put('/cities/1', json={"name": "Lyon", "country_code": "FR"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('City updated successfully', response.get_json()['message'])

        # Check if the city name was updated
        response = self.client.get('/cities/1')
        self.assertEqual(response.get_json()['name'], "Lyon")

    def test_delete_city(self):
        """Test deleting a city."""
        self.client.post('/cities', json={"id": "1", "name": "Paris", "country_code": "FR"})
        response = self.client.delete('/cities/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('City deleted successfully', response.get_json()['message'])

        # Check if the city was deleted
        response = self.client.get('/cities/1')
        self.assertEqual(response.status_code, 404)
        self.assertIn('City not found', response.get_json()['error'])

if __name__ == '__main__':
    unittest.main()
