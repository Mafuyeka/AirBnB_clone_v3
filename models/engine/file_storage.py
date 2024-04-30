# models/engine/file_storage.py

import json
from models.base_model import BaseModel

class FileStorage:
    """This class manages storage using JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return dictionary of all objects."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        else:
            return self.__objects

    def new(self, obj):
        """Add object to __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save objects to JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Load objects from JSON file."""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    cls_name, obj_id = k.split('.')
                    cls = eval(cls_name)
                    self.__objects[k] = cls(**v)
        except FileNotFoundError:
            pass
