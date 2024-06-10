#!/usr/bin/env python3

class Amenity:
    """class that inherits from BaseModel"""

    def __init__(self, amenity_id="", amenity_name=""):

        self.id = amenity_id
        self.name = amenity_name

    def __repr__(self):
        """String representation of the amenity"""
        return f"amenity {self.id} {self.name}"
