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
            "BaseModel","User", "City", "State", "Place",
            "Amenity", "Review"
            )

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

        except (FileNotFoundError, JSONDecodeError):
            pass

    def find_by_id(self, model, obj_id):
        """
        Method that Find and return an elemet by id.
        """

        m = FileStorage

        if model not in m.models:
            raise ModelNotFoundError(model)

        key = model + "." + obj_id

        if key not in m.__objects:
            raise InstanceNotFoundError(obj_id, model)

        return m.__objects[key]

    def delete_by_id(self, model, obj_id):
        """
        Method that Find and return an elemt by id.
        """

        t = FileStorage
        if model not in t.models:
            raise ModelNotFoundError(model)

        key = model + "." + obj_id
        if key not in t.__objects:
            raise InstanceNotFoundError(obj_id, model)

        del t.__objects[key]
        self.save()

    def find_all(self, model=""):
        """
        Method that find all instances of model.
        """

        if model and model not in FileStorage.models:
            raise ModelNotFoundError(model)
        result = []

        for key, val in FileStorage.__objects.items():
            if key.startswith(model):
                result.append(str(val))
        return result

    def update_one(self, model, iD, field, value):
        """
        Method that updates an instance.
        """
        m = FileStorage

        if model not in m.models:
            raise ModelNotFoundError(model)

        key = model + "." + iD

        if key not in m.__objects:
            raise InstanceNotFoundError(iD, model)

        if field in ("id", "updated_at", "created_at"):
            return

        instance = m.__objects[key]

        try:
            ftype = type(inst.__dict__[field])
            instance.__dict__[field] = ftype(value)
        except KeyError:
            instance.__dict__[field] = value
        finally:
            instance.updated_at = datetime.utcnow()
            self.save()
