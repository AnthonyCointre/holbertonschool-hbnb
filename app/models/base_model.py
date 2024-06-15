#!/usr/bin/env python3

import uuid
from datetime import datetime


class BaseModel:
    """
    Modèle de données représentant une entité.
    """

    def __init__(self):
        """
        Initialiser une instance de BaseModel.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convertir l'instance de BaseModel en un dictionnaire de données.
        """

        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
