from abc import ABC, abstractmethod
from typing import TypeVar, List, Generic

T = TypeVar('T')


class IPersistenceManager(ABC, Generic[T]):
    """Interface for the persistence manager"""
    @abstractmethod
    def get(self, cls, id) -> T:
        """Get an object by its class and id"""
        pass

    @abstractmethod
    def get_all(self, cls) -> List[T]:
        """Get all objects of a class"""
        pass

    @abstractmethod
    def save(self) -> None:
        """Save the current state of the session"""
        pass

    @abstractmethod
    def delete(self, obj=None) -> None:
        """Delete an object"""
        pass

    @abstractmethod
    def reload(self) -> None:
        """Reload the session"""
        pass

    @abstractmethod
    def close(self) -> None:
        """Close the session"""
        pass

    @abstractmethod
    def update(self, obj) -> None:
        """Update an object"""
        pass
