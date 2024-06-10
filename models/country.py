#!/usr/bin/python3

class City:
    def __init__(self, city_id, name, country):
        self.city_id = city_id
        self.name = name
        self.country = country

    def __repr__(self):
        return f"City({self.city_id}, {self.name}, {self.country})"
