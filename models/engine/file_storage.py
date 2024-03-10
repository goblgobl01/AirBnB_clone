#!/usr/bin/python3
"""
Module for file_storage.py
"""

import json


class FileStorage:
    """
    FileStorage class
    Attributes:
        __file_path: contains the path to
            the json file we're manipulating
        __objects: a dictionary that will contain
            every all the objects
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        The init method
        """
        pass

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj
        with key <obj class name>.id
        """
        variable = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[variable] = obj

    def save(self):
        """
        serializes __objects to
        the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as file:
            for key, value in FileStorage.__objects.items():
                FileStorage.__objects[key] = value.to_dict()
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.state import State
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = key.split('.')[0]
                    obj = eval(class_name)(**value)
                    self.new(obj)

        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
