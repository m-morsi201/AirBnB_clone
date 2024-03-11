#!/usr/bin/python3
"""
Module that define a Class user.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class user That inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
