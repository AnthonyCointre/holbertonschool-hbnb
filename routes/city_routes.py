#!/usr/bin/env python3


from flask import jsonify, request, Flask
from flask_restful import Resource, Api
from models.city import City
from models.country import Country


class cityCollectionResource(Resource):
    def __init__(self):
        """ Pre-loaded countries for validation"""
        self.city_collection = CityCollection()

        self.countries = [
            Country(country_id="US", country_name="United States"),
            Country(country_id="FR", country_name="France")
        ]

    def get(self):
        """  Get all cities"""
        return jsonify([city.to_dict() for city in self.city_collection.cities])

    def post(self):
        """Add a new city"""
        data = request.get_json()
        country_code = data.get("country_code")
        if country_code is None:
            return jsonify({"error": "Missing country_code"}), 400

        new_city = City(city_id=data.get("id"), city_name=data.get(
            "name"), city_country=country_code)
        self.city_collection.add(new_city)
        return {"message": "City added successfully"}, 201


class cityResource(Resource):
    def __init__(self):
        """ Pre-loaded countries for validation"""
        self.city_collection = CityCollection()

    def get(self, city_id):
        """ Get a city by id"""
        city = self.city_collection.get(city_id)
        if city is not None:
            return jsonify(city.to_dict())
        else:
            return jsonify({"error": "City not found"}), 404

    def put(self, city_id):
        """update city by id"""
        data = request.get_json()
        city = self.city_collection.get(city_id)
        if city is not None:
            city.name = data.get("name")
            city.country = data.get("country_code")
            return {"message": "City updated successfully"}, 200
        else:
            return {"message": "City not found"}, 404

    def delete(self, city_id):
        """delete city by id"""
        city = self.city_collection.get(city_id)
        if city is not None:
            self.city_collection.delete(city)
            return {"message": "City deleted successfully"}, 200
        else:
            return {"message": "City not found"}, 404
