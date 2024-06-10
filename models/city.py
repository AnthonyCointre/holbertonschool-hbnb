#!/usr/bin/env python3

class City(BaseModel):
    """class that inherits from BaseModel"""

    def __init__(self, city_id="", city_name="", city_country=""):
        self.id = city_id
        self.name = city_name
        self.country = city_country

    def add(self):
        """Add a city"""
        self.city.append(city)
