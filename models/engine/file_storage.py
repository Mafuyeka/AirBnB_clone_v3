import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        pass

    def new(self, obj):
        pass

    def save(self):
        pass

    def reload(self):
        pass

    def delete(self, obj=None):
        pass

    def get(self, cls, id):
        """Retrieve one object"""
        pass

    def count(self, cls=None):
        """Count the number of objects in storage"""
        pass
