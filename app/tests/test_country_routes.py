#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask.testing import FlaskClient
from flask_restful import Api
from app.routes.country_routes import CountryList

class TestCountryList(unittest.TestCase):

    def setUp(self):
        """ Set up test environment """
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(CountryList, '/countries')
        self.client = self.app.test_client()

        # Preload mock countries
        self.mock_countries = [
            CountryList(country_id="US", name="United States"),
            CountryList(country_id="FR", name="France")
        ]
        
        # Mock Country.get method
        CountryList.get = MagicMock(side_effect=self.mock_get_country)

    def mock_get_country(self, country_code):
        """ Mocked Country.get method """
        for country in self.mock_countries:
            if country.country_id == country_code:
                return country
        return None

    def test_get_all_countries(self):
        """ Test GET /countries endpoint """
        response = self.client.get('/countries')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), len(self.mock_countries))
        for country_data, expected_country in zip(data, self.mock_countries):
            self.assertEqual(country_data['country_id'], expected_country.country_id)
            self.assertEqual(country_data['name'], expected_country.name)

    def test_get_existing_country(self):
        """ Test GET /countries/<country_code> for an existing country """
        country_code = "US"
        response = self.client.get(f'/countries/{country_code}')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['country_id'], country_code)
        self.assertEqual(data['name'], "United States")

    def test_get_non_existing_country(self):
        """ Test GET /countries/<country_code> for a non-existing country """
        country_code = "XX"  # Assuming "XX" is not in mock_countries
        response = self.client.get(f'/countries/{country_code}')
        self.assertEqual(response.status_code, 404)
        data = response.json
        self.assertEqual(data['error'], "Country not found")

if __name__ == '__main__':
    unittest.main()