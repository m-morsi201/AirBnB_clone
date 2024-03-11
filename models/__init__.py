#!/usr/bin/python3

"""
__init__ method for organize models package.
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
