#!/usr/bin/python3
"""
This module defines unittests for models/user.py.
"""

import os
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Unittests for testing instantiation of the User class.
    """

    @classmethod
    def setUp_Class(cls):
        """
        Class method that testing instantiation.
        """
        cls.MyUser = User()
        cls.MyUser.first_name = "FristName"
        cls.MyUser.last_name = "LastName"
        cls.MyUser.email = "usrname@email.com"
        cls.MyUser.password = "password"

    @classmethod
    def tearDown_Class(cls):
        """
        Class method that remove inctance.
        """

        del cls.MyUser

        try:
            os.remove("file.json")

        except FileNotFoundError:
            pass

    def is_subclass_test(self):
        """
        Mehtod to checks is subclass.
        """

        self.assertTrue(issubclass(self.MyUser.__class__, BaseModel), True)

    def test_func(self):
        """
        Method to check for function.
        """

        self.assertIsNotNone(User.__doc__)
    
    def tes_attr(self):
        self.assertEqual(MyUser.email, '')
        self.assertEqual(MyUser.password, '')
        self.assertEqual(MyUser.first_name, '')
        self.assertEqual(MyUser.last_name, '')
        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')
        self.assertEqual(User.first_name, '')
        self.assertEqual(User.last_name, '')

    def test_to_dict(self):
        """
        Method to checks for dict.
        """
        MyUser = User()
        NewDict = MyUser.to_dict()
        self.assertEqual(type(NewDict), dict)

        for i in MyUser.__dict__:
            self.assertTrue(i in NewDict)
            self.assertTrue("__class__" in NewDict)

    def TestAttr(self):
        """
        Method to check if it has attributes.
        """

        self.assertTrue('email' in self.MyUser.__dict__)
        self.assertTrue('id' in self.MyUser.__dict__)
        self.assertTrue('created_at' in self.MyUser.__dict__)
        self.assertTrue('updated_at' in self.MyUser.__dict__)
        self.assertTrue('password' in self.MyUser.__dict__)
        self.assertTrue('first_name' in self.MyUser.__dict__)
        self.assertTrue('last_name' in self.MyUser.__dict__)

    def test_save(self):
        """
        Method to check a save.
        """
        
        MyUser = User()
        MyUser.save()
        self.assertNotEqual(MyUser.created_at, MyUser.updated_at)


if __name__ == "__main__":
    unittest.main()
