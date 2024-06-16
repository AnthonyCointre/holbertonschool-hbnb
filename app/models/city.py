#!/usr/bin/env python3

from datetime import datetime
from app.models.base_model import BaseModel


class City(BaseModel):

    def __init__(self, name, country_id, data_manager):
        super().__init__()
        self._name = name
        self._country_id = country_id
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        city = City(
            name=data['city_name'],
            country_id=data['country_id'],
            data_manager=data_manager
        )
        city.id = data['city_id']
        city.created_at = datetime.fromisoformat(data['created_at'])
        city.updated_at = datetime.fromisoformat(data['updated_at'])
        return city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.save()

    @property
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, value):
        self._country_id = value
        self.save()

    def to_dict(self):
        return {
            "city_id": self.id,
            "city_name": self._name,
            "country_id": self._country_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
