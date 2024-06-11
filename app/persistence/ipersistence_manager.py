#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import TypeVar, List, Generic

T = TypeVar('T')


class IPersistenceManager(ABC, Generic[T]):
    """
    IPersistenceManager est une classe de base abstraite définissant des méthodes pour la gestion de la persistance.
    """

    @abstractmethod
    def get(self, cls, id) -> T:
        """
        Récupère un objet de la classe spécifiée avec l'identifiant donné.
        """

        pass

    @abstractmethod
    def get_all(self, cls) -> List[T]:
        """
        Récupère tous les objets de la classe spécifiée.
        """

        pass

    @abstractmethod
    def save(self) -> None:
        """
        Enregistre les modifications apportées aux données.
        """

        pass

    @abstractmethod
    def delete(self, obj=None) -> None:
        """
        Supprime l'objet spécifié ou tous les objets si aucun argument n'est fourni.
        """

        pass

    @abstractmethod
    def reload(self) -> None:
        """
        Recharge les données.
        """

        pass

    @abstractmethod
    def close(self) -> None:
        """
        Ferme le gestionnaire de persistance.
        """

        pass

    @abstractmethod
    def update(self, obj) -> None:
        """
        Met à jour l'objet spécifié.
        """

        pass
