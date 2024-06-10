#!/usr/bin/env python3

class BaseModel:
    def __init__(self, id,  name="", date_creation=""):
        self.id = id
        self.name = name
        self.date_creation = date_creation

    def print(self):
        print(f"id: {self.id}, name: {
              self.name}, date_creation: {self.date_creation}")

    def save(self):
        """save obj in datat base"""
        print("save")

    def delete(self):
        """delete object in data base"""
        print("delete")
