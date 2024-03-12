#!/usr/bin/python3
"""
this Module define a unittest for Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Method to define a unittest for Review class
    """

    def test_object_Instantiation(self):
        """
        Method to checks an instantiates class.
        """

        self.my_review = Review()

    def test_attr(self):
        """
        Method to checks an test Class: Review attributes.
        """

        self.my_review = Review()
        self.assertTrue(hasattr(self.my_review, "created_at"))
        self.assertTrue(hasattr(self.my_review, "updated_at"))
        self.assertFalse(hasattr(self.my_review, "random_attr"))
        self.assertTrue(hasattr(self.my_review, "text"))
        self.assertTrue(hasattr(self.my_review, "id"))
        self.assertEqual(self.my_review.text, "")
        self.assertEqual(self.my_review.__class__.__name__, "Review")

    def test_save(self):
        """
        Method to checks an testing method: save
        """

        self.my_review = Review()
        self.my_review.save()
        self.assertTrue(hasattr(self.my_review, "updated_at"))

    def teststr(self):
        """
        Method to checks an testing __str__ return format of BaseModel.
        """

        self.my_review = Review()
        s = "[{}] ({}) {}".format(self.my_review.__class__.__name__,
                                  str(self.my_review.id),
                                  self.my_review.__dict__)
        self.assertEqual(print(s), print(self.my_review))


if __name__ == '__main__':
    unittest.main()
