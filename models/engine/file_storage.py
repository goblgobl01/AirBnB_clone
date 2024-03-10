#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        variable = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[variable] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as file:
            for key, value in FileStorage.__objects.items():
                FileStorage.__objects[key] = value.to_dict()
            json.dump(FileStorage.__objects, file)

    def reload(self):
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
