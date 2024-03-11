#!/usr/bin/python3
"""
Module that defines  stateModel class.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    class that define a stat.
    that inherits from BaseModel.
    """

    name: str = ''
