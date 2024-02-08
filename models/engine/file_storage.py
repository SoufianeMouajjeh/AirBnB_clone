#!/usr/bin/python3
"""
class FileStorage
"""
import json
import os
from datetime import datetime


class FileStorage:
    """
    class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        all
        """
        return self.__objects

    def new(self, obj):
        """
        new
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """
        save
        """
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        reload
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                dict = json.load(f)
                for k, v in dict.items():
                    class_name = v["__class__"]
                    if class_name in globals():
                        object_class = globals()[class_name]
                        print(object_class)
                        del v["__class__"]
                        object = object_class(**v)
                        FileStorage.__objects[k] = object
                    else:
                        from models.base_model import BaseModel
                        from models.user import User
                        from models.state import State
                        from models.city import City
                        from models.place import Place
                        from models.amenity import Amenity
                        from models.review import Review

                        object = eval(k.split('.')[0])(**v)
                        FileStorage.__objects[k] = object
        except FileNotFoundError:
            pass
