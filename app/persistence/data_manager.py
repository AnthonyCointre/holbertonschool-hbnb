#!/usr/bin/python3

import os
import json
from app.persistence.ipersistence_manager import IPersistenceManager


class DataManager(IPersistenceManager):

    def __init__(self, data_file):
        self.storage = {}
        self.data_file = data_file
        self.create_directory_if_not_exists()
        self.load_from_json()

    def create_directory_if_not_exists(self):
        directory = os.path.dirname(self.data_file)

        if not os.path.exists(directory):
            os.makedirs(directory)

    def load_from_json(self):
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for entity_type, entities in data.items():
                    self.storage[entity_type] = {}
                    for entity_id, entity_data in entities.items():
                        try:
                            entity = self.dict_to_entity(
                                entity_type, entity_data)
                            self.storage[entity_type][entity_id] = entity
                        except ValueError as e:
                            print(f"Skipping invalid {entity_type}: {e}")
        except FileNotFoundError:
            self.storage = {}

    def dict_to_entity(self, entity_type, entity_data):
        module = __import__('app.models.' + entity_type.lower(),
                            fromlist=[entity_type])
        entity_class = getattr(module, entity_type)
        return entity_class.from_dict(entity_data, self)

    def save(self, entity):
        entity_type = type(entity).__name__

        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity.id] = entity
        self.save_to_json()
        return entity

    def get(self, entity_id, entity_type):
        if entity_type in self.storage \
                and entity_id in self.storage[entity_type]:
            return self.storage[entity_type][entity_id]
        return None

    def update(self, entity):

        entity_type = type(entity).__name__
        if entity_type in self.storage \
                and entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity
            self.save_to_json()
            return entity
        return None

    def delete(self, entity_id, entity_type):

        if entity_type in self.storage \
                and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            self.save_to_json()
            return True
        return False

    def save_to_json(self, file_path=None):

        if not file_path:
            file_path = self.data_file
        serializable_storage = {}
        for entity_type, entities in self.storage.items():
            entity_dict = {}
            for entity_id, entity in entities.items():
                entity_data = entity.to_dict()
                entity_dict[entity_id] = entity_data
            serializable_storage[entity_type] = entity_dict
        with open(file_path, 'w') as file:
            json.dump(serializable_storage, file, indent=4)
