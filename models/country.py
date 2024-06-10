#!/usr/bin/env python3
from models.base_model import BaseModel


class country(BaseModel):
    """class that inherits from BaseModel"""
    def __init__(self, country_id="", country_name=""):
        self.id = country_id
        self.name = country_name
        
    def add(self):
        """Add a country"""
        self.country.append(country)
