#!/usr/bin/env python3

from app.models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []

    def to_dict(self):
        amenity_dict = super().to_dict()
        amenity_dict.update({
            "name": self.name,
            "places": [place.id for place in self.places]
        })
        return amenity_dict

    def __repr__(self):
        return f"<Amenity {self.name}>"
