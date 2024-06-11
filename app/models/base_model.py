#!/usr/bin/env python3


class BaseModel:
    """
    Classe de base pour modéliser les entités communes.
    """

    def __init__(self, id, name="", date_creation=""):
        """
        Initialise une nouvelle instance de BaseModel.
        """

        self.id = id
        self.name = name
        self.date_creation = date_creation

    def print(self):
        """
        Affiche les attributs de l'entité sous forme de chaîne de caractères.
        """

        print(f"id: {self.id}, name: {self.name}, date_creation: {self.date_creation}")

    def save(self):
        """
        Simule la sauvegarde de l'entité dans une base de données.
        """

        print("save")

    def delete(self):
        """
        Simule la suppression de l'entité dans une base de données.

        """

        print("delete")
