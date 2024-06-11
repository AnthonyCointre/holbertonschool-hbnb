#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Classe Review qui hérite de BaseModel.
    """

    def __init__(self, review_id, user, place):
        """
        Initialise une nouvelle instance de Review.
        """

        super().__init__(review_id)
        self.review_id = review_id
        self.user = user
        self.place = place

    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de l'avis.
        """

        return f"Review({self.review_id}, {self.user}, {self.place})"
