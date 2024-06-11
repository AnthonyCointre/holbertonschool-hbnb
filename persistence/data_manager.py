#!/usr/bin/python3

from typing import List, Type, Any
from persistence.ipersistence_manager import IPersistenceManager


class DataManager(IPersistenceManager):
    """
    DataManager class implements the IPersistenceManager interface and provides methods for managing data.
    """

    def __init__(self):
        """
        Initializes the DataManager object.
        """

        super().__init__()

    def get(self, cls: Type[Any], id: Any) -> Any:
        """
        Retrieves an object of the specified class with the given id.
        """

        pass

    def get_all(self, cls: Type[Any]) -> List[Any]:
        """
        Retrieves all objects of the specified class.
        """

        pass

    def save(self):
        """
        Saves changes to the data.
        """

        pass

    def delete(self, obj: Any = None) -> None:
        """
        Deletes the specified object or all objects if no argument is provided.
        """

        pass

    def reload(self):
        """
        Reloads the data.
        """

        pass

    def close(self):
        """
        Closes the data manager.
        """

        pass
