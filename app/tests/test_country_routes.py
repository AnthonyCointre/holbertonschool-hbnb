#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask.testing import FlaskClient
from flask_restful import Api
from app.routes.country_routes import CountryList, CountryResource

class TestCountryList(unittest.TestCase):
    def setUp(self):
        # Create a Flask app and configure it for testing
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.api = Api(self.app)
        
        # Add resource to the API
        self.api.add_resource(CountryResource, '/countries', '/countries/<string:country_code>')
        
        # Initialize the test client
        self.client = self.app.test_client()

        # Mock countries data
        self.mock_countries = [
            CountryList(country_id="US", name="United States"),
            CountryList(country_id="CA", name="Canada"),
        ]

        # Patch the CountryList.get method to use the mock data
        CountryList.get = MagicMock(side_effect=self.mock_get_country)

    def mock_get_country(self, country_code):
        """ Mocked Country.get method """
        for country in self.mock_countries:
            if country.country_id == country_code:
                return country
        return None

    @patch('app.routes.country_routes.CountryList.get_all')
    def test_get_all_countries(self, mock_get_all):
        """ Test GET /countries endpoint """
        mock_get_all.return_value = self.mock_countries
        response = self.client.get('/countries')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), len(self.mock_countries))
        for country_data, expected_country in zip(data, self.mock_countries):
            self.assertEqual(country_data['country_id'], expected_country.country_id)
            self.assertEqual(country_data['name'], expected_country.name)

    def test_get_existing_country(self):
        """ Test GET /countries/<country_code> for an existing country """
        country_code = "US"
        response = self.client.get(f'/countries/{country_code}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['country_id'], country_code)
        self.assertEqual(data['name'], "United States")

    def test_get_non_existing_country(self):
        """ Test GET /countries/<country_code> for a non-existing country """
        country_code = "XX"
        response = self.client.get(f'/countries/{country_code}')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['error'], "Country not found")

if __name__ == '__main__':
    unittest.main()
