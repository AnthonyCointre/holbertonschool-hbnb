#!/usr/bin/env python3

from app.models.base_model import BaseModel


class Review(BaseModel):
    """
    Modèle de données représentant une critique.
    """

    def __init__(self, place_id, user_id, rating, comment):
        """
        Initialiser une instance de Review.
        """

        super().__init__()
        self._place_id = place_id
        self._user_id = user_id
        self._rating = rating
        self._comment = comment

    def to_dict(self):
        """
        Convertir l'instance de Review en un dictionnaire de données.
        """

        return {
            "review_id": self.id,
            "place_id": self._place_id,
            "user_id": self._user_id,
            "rating": self._rating,
            "comment": self._comment,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
