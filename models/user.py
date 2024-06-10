#!/usr/bin/env python3
from models.base_model import BaseModel


class user(BaseModel):
    """class that inherits from BaseModel"""


def _init_(self, user_first_name="", user_last_name="", user_email=""):

    self.email = user_email
    self.first_name = user_first_name
    self.last_name = user_last_name


def add_place(self, place_id):
    """Add a place to the user"""
    if place_id not in self.places:
        self.places.append(place_id)


def __repr__(self):
    """String representation of the user"""
    return f"user {self.id} {self.email} {self.first_name} {self.last_name}"
