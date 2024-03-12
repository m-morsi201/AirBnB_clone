#!/usr/bin/python3
"""
This module is a test for BaseModel class.
"""

import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """
    class that define Test cases for base_model.py
    """

    def test_methods(self):
        """
        Method to checking a function.
        """

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_str(self):
        """
        Method to checks the __str__ output of BaseModel.
        """

        self.base = BaseModel()
        b = "[{}] ({}) {}".format(self.base.__class__.__name__,
                                  str(self.base.id),
                                  self.base.__dict__)
        self.assertEqual(print(b), print(self.base))

    def test_to_dict(self):
        """
        Method to checks the to_dict() function of BaseModel.
        """

        base1 = BaseModel()
        PrevTime = base1.updated_at
        self.assertDictEqual(base1.to_dict(),
                             {'__class__': type(base1).__name__,
                              'updated_at': base1.updated_at.isoformat(),
                              'id': base1.id,
                              'created_at': base1.created_at.isoformat()})
        base1.save()
        self.assertNotEqual(PrevTime, base1.updated_at)

    def test_attr_classes(self):
        """
        Method that checks user attributes.
        """

        base1 = BaseModel()
        base2 = BaseModel()
        self.assertTrue(hasattr(base1, "created_at"))
        self.assertTrue(hasattr(base1, "updated_at"))
        self.assertFalse(hasattr(base1, "random_attr"))
        self.assertFalse(hasattr(base1, "name"))
        self.assertTrue(hasattr(base1, "id"))
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)
        self.assertNotEqual(base1.id, base2.id)

    def test_save(self):
        """
        Method to checks the save method.
        """

        base = BaseModel()
        prev_time = base.updated_at
        base.save()
        self.assertTrue(hasattr(base, "updated_at"))
        new_time = base.updated_at
        self.assertNotEqual(prev_time, new_time)


if __name__ == '__main__':
    unittest.main()
