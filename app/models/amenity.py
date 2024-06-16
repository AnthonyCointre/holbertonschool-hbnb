#!/usr/bin/env python3

from datetime import datetime
from app.models.base_model import BaseModel


class Amenity(BaseModel):

    def __init__(self, name, data_manager):
        super().__init__()
        self._name = name
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        amenity = Amenity(
            name=data['amenity_name'],
            data_manager=data_manager
        )
        amenity.id = data['amenity_id']
        amenity.created_at = datetime.fromisoformat(data['created_at'])
        amenity.updated_at = datetime.fromisoformat(data['updated_at'])
        return amenity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.save()

    def to_dict(self):
        return {
            "amenity_id": self.id,
            "amenity_name": self._name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
