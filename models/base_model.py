#!/usr/bin/python3

"""
This module defines all common attributes/methods for other classes
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    The base class for all common attributes/methods
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of a Base instance with:
            id, creation and update dates.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Method that returns a readable string representation
        of BaseModel.
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """
        Method that updates the public instance attribute updated_at
        with the current datetime.
        """

        self.__dict__.update({'updated_at': datetime.now()})
        models.storage.save()

    def to_dict(self):
        """
        Method that returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """

        MyDict = self.__dict__.copy()
        MyDict['__class__'] = self.__class__.__name__
        MyDict['created_at'] = self.created_at.isoformat()
        MyDict['updated_at'] = self.updated_at.isoformat()
        return(MyDict)

    @classmethod
    def all(cls):
        """
        Class Method that Retrieve all current instances of cls.
        """

        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """
        class method that Get the number
        of all current instances of cls.
        """

        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """
        Class Method that creates an Instance.
        """

        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """
        Class Method thar retrieve an instance.
        """

        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """
        class method that deletes an instance.
        """

        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """
        class method that updates an instance.
        """

        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__, instance_id, *arg
            )
