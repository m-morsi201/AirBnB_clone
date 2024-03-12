#!/usr/bin/python3

"""
This module defines the storage system.
Useing JSON format (serialize and deserialize objects).
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    """
    filestorage class will serve as an Object.
    """

    __objects: dict = {}
    __file_path: str = 'file.json'
    models = (
            "BaseModel", "User", "City", "State", "Place",
            "Amenity", "Review")

    def __init__(self):
        """
        constructor to filestorage class.
        """

        pass

    def all(self):
        """
        method that Return all instances that stored.
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Method to Stores a new Object.
        """

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Method to serializes objects stored and persist in file.
        """

        serialized = {
            key: val.to_dict()
            for key, val in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(serialized))

    def reload(self):
        """
        Method that de-serialize persisted objects.
        """

        try:
            deserialized = {}

            with open(FileStorage.__file_path, "r") as f:
                deserialized = json.loads(f.read())

            FileStorage.__objects = {
                key:
                    eval(obj["__class__"])(**obj)
                    for key, obj in deserialized.items()}

        except (FileNotFoundError):
            pass
