#!/usr/bin/python3
"""
Module that define City model.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    class that define city model.
    it inherits from BaseMode.
    """

    state_id: str = ''
    name: str = ''
