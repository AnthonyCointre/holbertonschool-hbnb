#!/usr/bin/env python3

from app.models.base_model import BaseModel


class User(BaseModel):
    """
    Modèle de données représentant un utilisateur.
    """

    def __init__(self, email, first_name, last_name):
        """
        Initialiser une instance de User.
        """

        super().__init__()
        self._email = email
        self._first_name = first_name
        self._last_name = last_name

    def to_dict(self):
        """
        Convertir l'instance de User en un dictionnaire de données.
        """

        return {
            "user_id": self.id,
            "email": self._email,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
