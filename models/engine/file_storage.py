#!/usr/bin/python3
"""
This module defines the FileStorage class, a simple JSON-based storage.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return type(self).__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(type(self).__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in type(self).__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(type(self).__file_path, "r", encoding="utf-8") as f:
                type(self).__objects = {k: BaseModel(**v) for k, v in json.load(f).items()}
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload() method for deserializing the JSON file to objects."""
        self.reload()
