#!/usr/bin/env python3

from datetime import datetime
from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, name, description, address, city, latitude, longitude, num_rooms, num_bathrooms, price_per_night, max_guests):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = []
        self.reviews = []
        self.host = None

    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)
            review.place = self
            review.updated_at = datetime.now()

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            amenity.places.append(self)
            amenity.updated_at = datetime.now()

    def to_dict(self):
        place_dict = super().to_dict()
        place_dict.update({
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "city": self.city.id if self.city else None,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "num_rooms": self.num_rooms,
            "num_bathrooms": self.num_bathrooms,
            "price_per_night": self.price_per_night,
            "max_guests": self.max_guests,
            "amenities": [amenity.id for amenity in self.amenities],
            "reviews": [review.id for review in self.reviews],
            "host": self.host.id if self.host else None
        })
        return place_dict

    def __repr__(self):
        return f"<Place {self.name}>"
