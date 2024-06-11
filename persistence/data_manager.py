#!/usr/bin/python3

from typing import List, Type, Any
from persistence.ipersistence_manager import IPersistenceManager


class DataManager(IPersistenceManager):
    """
    La classe DataManager implémente l'interface IPersistenceManager et fournit des méthodes pour gérer les données.
    """

    def __init__(self):
        """
        Initialise l'objet DataManager.
        """

        super().__init__()

    def get(self, cls: Type[Any], id: Any) -> Any:
        """
        Récupère un objet de la classe spécifiée avec l'identifiant donné.
        """

        pass

    def get_all(self, cls: Type[Any]) -> List[Any]:
        """
        Récupère tous les objets de la classe spécifiée.
        """

        pass

    def save(self):
        """
        Enregistre les modifications apportées aux données.
        """

        pass

    def delete(self, obj: Any = None) -> None:
        """
        Supprime l'objet spécifié ou tous les objets si aucun argument n'est fourni.
        """

        pass

    def reload(self):
        """
        Recharge les données.
        """

        pass

    def close(self):
        """
        Ferme le gestionnaire de données.
        """

        pass
