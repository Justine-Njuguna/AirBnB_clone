#!/usr/bin/python3


import json
import os
from os.path import exists
import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Reloads the stored objects"""
        from models.user import User
        from models.base_model import BaseModel
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review


        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                if class_name == 'User':
                    self.__objects[key] = User(**value)

                elif class_name == 'Place':
                    self.__objects[key] = Place(**value)

                elif class_name == 'State':
                    self.__objects[key] = State(**value)
                
                elif class_name == 'City':
                    self.__objects[key] = City(**value)
                
                elif class_name == 'Amenity':
                    self.__objects[key] = Amenity(**value)
                
                elif class_name == 'Review':
                    self.__objects[key] = Review(**value)
                
                else:
                    cls = eval(class_name)
                    self.__objects[key] = cls(**value)


#from models.base_model import BaseModel
#from .engine.file_storage
