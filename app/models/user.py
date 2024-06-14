#!/usr/bin/env python3

from datetime import datetime
from app.models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = []

    def update_profile(self, first_name=None, last_name=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        self.updated_at = datetime.now()

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
            place.host = self
            place.updated_at = datetime.now()

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.update({
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "places": [place.id for place in self.places]
        })
        return user_dict

    def __repr__(self):
        return f"<User {self.email}>"
