#!/usr/bin/env python3

from app.models.base_model import BaseModel


class Country(BaseModel):
    """
    Modèle de données représentant un pays.
    """

    def __init__(self, name, code):
        """
        Initialiser une instance de Country.
        """

        super().__init__()
        self._name = name
        self._code = code

    def to_dict(self):
        """
        Convertir l'instance de Country en un dictionnaire de données.
        """

        return {
            "country_id": self.id,
            "name": self._name,
            "code": self._code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
