#!/usr/bin/python3
"""
This Module define a Unittest for FileStorage class
"""

import os
import unittest
from models import storage
from models.user import User
from models.engine import file_storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):
    """
    class that define a Unittest for FileStorage class.
    """

    def FileStorage_Instantiation(self):
        """
        Method to checks instantiation of the FileStorage class.
        """

        tobj = FileStorage()
        self.assertEqual(type(FileStorage()), FileStorage)
        self.assertIsInstance(tobj, FileStorage)

    def all_test(self):
        """
        Method to checks all.
        """
        self.assertEqual(dict, type(models.storage.all()))
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def Access_test(self):
        """
        Mehod to checks  read permission and write permissions.
        """

        read_per = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read_per)
        write_per = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write_per)
        excute_per = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertFalse(excute_per)

    def new_test(self):
        """
        Method to checks saves new object into dictionary
        """

        n_usr.name = "AnyName"
        n_usr.id = 123456
        f_strg = FileStorage()
        instDic = f_strg.all()
        n_usr = User()
        f_strg.new(n_usr)
        key = n_usr.__class__.__name__ + "." + str(n_usr.id)
        self.assertIsNotNone(instDic[key])

    def reload_test(self):
        """
        Method checks reload objects.
        """

        f_strg = FileStorage()
        try:
            os.remove("file.json")
        except():
            continue
        with open("file.json", "w") as W:
            W.write("{}")
        with open("file.json", "r") as R:
            for i in R:
                self.assertEqual(i, "{}")
        self.assertIs(f_strg.reload(), None)

    def docs_test(self):
        """
        Method chaecks docstring of functions.
        """

        for i in dir(FileStorage):
            self.assertTrue(len(i.__doc__) > 0)

    def save_test(self):
        """
        Method to checks for save method.
        """

        f_strg1 = BaseModel()
        f_strg2 = FileStorage()
        f_strg2.new(f_strg1)
        dict1 = f_strg2.all()
        f_strg2.save()
        f_strg2.reload()
        dict2 = f_strg2.all()

        for i in dict1:
            key1 = i

        for j in dict2:
            key2 = j

        self.assertEqual(dict1[key1].to_dict(), dict2[key2].to_dict())


if __name__ == '__main__':
    unittest.main()
