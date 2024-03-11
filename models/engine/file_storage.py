#!/usr/bin/python3

"""
This module is the storage system.
"""


from datetime import datetime
import json
import os.path

class FileStorage:
    """
    That serializes instances to a JSON file and deserializes JSON file.
    """

    __objects = {}
    __file_path = "file.json"

    def __init__(self):
        """
        constructor for FileStorage class
        """

        pass

    def all(self):
        """
        Method that returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        """

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
