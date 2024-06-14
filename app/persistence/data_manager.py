#!/usr/bin/python3

from app.persistence.ipersistence_manager import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def save(self, entity):
        self.storage[(entity.id, type(entity).__name__)] = entity

    def get(self, entity_id, entity_type):
        return self.storage.get((entity_id, entity_type), None)

    def update(self, entity):
        if (entity.id, type(entity).__name__) in self.storage:
            self.storage[(entity.id, type(entity).__name__)] = entity
        else:
            raise ValueError(
                f"{type(entity).__name__} with id {entity.id} does not exist.")

    def delete(self, entity_id, entity_type):
        if (entity_id, entity_type) in self.storage:
            del self.storage[(entity_id, entity_type)]
        else:
            raise ValueError(
                f"{entity_type} with id {entity_id} does not exist.")
