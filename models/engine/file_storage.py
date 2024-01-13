#!/usr/bin/python3
"""
FileStorage module
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """for sorting and restore data"""

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Sets an object in the __objects"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def all(self):
        """the dictionary __objects"""
        return self.__objects

    def save(self):
        """save __objects to the JSON file"""
        objs = {}
        for key in self.__objects:
            objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(objs, f)

    def reload(self):
        """import JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for key in objs:
                self.__objects[key] = classes[objs[key]["__class__"]](**objs[key])
        except:
            pass
