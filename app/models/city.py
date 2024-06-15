#!/usr/bin/env python3

from app.models.base_model import BaseModel


class City(BaseModel):
    """
    Modèle de données représentant une ville.
    """

    def __init__(self, name, country_code):
        """
        Initialiser une instance de City.
        """

        super().__init__()
        self._name = name
        self._country_code = country_code

    def to_dict(self):
        """
        Convertir l'instance de City en un dictionnaire de données.
        """

        return {
            "city_id": self.id,
            "name": self._name,
            "country_code": self._country_code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
