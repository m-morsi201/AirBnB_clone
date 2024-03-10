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

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key not in ['__class__']:
                    setattr(self, key, value)

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

        self.updated_at = datetime.now()

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
