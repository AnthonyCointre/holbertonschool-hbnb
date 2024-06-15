#!/usr/bin/env python3

from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Modèle de données représentant une commodité.
    """

    def __init__(self, name):
        """
        Initialiser une instance de Amenity.
        """

        super().__init__()
        self._name = name

    def to_dict(self):
        """
        Convertir l'instance de Amenity en un dictionnaire de données.
        """

        return {
            "amenity_id": self.id,
            "name": self._name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
