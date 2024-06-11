#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import TypeVar, List, Generic

T = TypeVar('T')


class IPersistenceManager(ABC, Generic[T]):
    """
    IPersistenceManager is an abstract base class defining methods for persistence management.
    """

    @abstractmethod
    def get(self, cls, id) -> T:
        """
        Retrieves an object of the specified class with the given id.
        """

        pass

    @abstractmethod
    def get_all(self, cls) -> List[T]:
        """
        Retrieves all objects of the specified class.
        """

        pass

    @abstractmethod
    def save(self) -> None:
        """
        Saves changes to the data.
        """

        pass

    @abstractmethod
    def delete(self, obj=None) -> None:
        """
        Deletes the specified object or all objects if no argument is provided.
        """

        pass

    @abstractmethod
    def reload(self) -> None:
        """
        Reloads the data.
        """

        pass

    @abstractmethod
    def close(self) -> None:
        """
        Closes the persistence manager.
        """

        pass

    @abstractmethod
    def update(self, obj) -> None:
        """
        Updates the specified object.
        """

        pass
