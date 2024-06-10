#!/usr/bin/env python3

class place:
    """class that inherits from BaseModel"""

    def _init_(self, place_id="", place_name="", place_description="", place_address="", place_city="", place_country="", place_owner_id=""):

        self.id = place_id
        self.name = place_name
        self.description = place_description
        self.address = place_address
        self.city = place_city
        self.country = place_country
        self.owner_id = place_owner_id


def add_review(self, review):
    """Add a review to the place"""
    self.reviews.append(review)


def add_amenity(self, amenity):
    """Add an amenity to the place"""
    self.amenities.append(amenity)


def _repr_(self):
    """String representation of the place"""
    return f"place {self.id} {self.name} {self.description} {self.address} {self.city} {self.country} {self.owner_id}"
