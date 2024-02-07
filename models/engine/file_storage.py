#!/usr/bin/python3
"""
class FileStorage
"""
import json
import os
from models.base_model import BaseModel


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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                self.__objects = {k: BaseModel(**v) for k, v in json.load(f).items()}