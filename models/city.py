#!/usr/bin/env python3
from models.base_model import BaseModel


class City(BaseModel):
    """class that inherits from BaseModel"""

    def __init__(self, city_id="", city_name="", city_country=""):
        self.id = city_id
        self.name = city_name
        self.country = city_country

    def __repr__(self):
        """String representation of the city"""
        return f"city {self.id} {self.name} {self.country}"


class CityCollection:
    """a collection of cities"""

    def __init__(self):
        self.cities = []

    def add(self, city):
        """Add a city to a collection of cities"""
        self.cities.append(city)
