#!/usr/bin/python3
"""
Module that define a review module.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review model.
    That inherits from BaseModel.
    """

    place_id = ""
    user_id = ""
    text = ""
