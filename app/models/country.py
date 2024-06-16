#!/usr/bin/env python3

from datetime import datetime
from app.models.base_model import BaseModel


class Country(BaseModel):

    def __init__(self, name, code=None):
        super().__init__()
        self._name = name
        self._code = code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def from_dict(data, data_manager):
        country = Country(
            name=data['name'],
            code=data.get('code', None)
        )
        country.id = data['country_id']
        country.created_at = datetime.fromisoformat(data['created_at'])
        country.updated_at = datetime.fromisoformat(data['updated_at'])
        return country

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.updated_at = datetime.now()

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "country_id": self.id,
            "name": self._name,
            "code": self._code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
