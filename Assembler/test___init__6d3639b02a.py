from __future__ import print_function
import sys
import unittest


class MyClass:
    def __init__(self, token, t):
        self.token = token
        self.t = t


class TestMyClass(unittest.TestCase):
    def test_init_success(self):
        token = "my_token"
        t = 10
        my_obj = MyClass(token, t)
        self.assertEqual(my_obj.token, token, "Token should be equal to the provided value")
        self.assertEqual(my_obj.t, t, "t should be equal to the provided value")

    def test_init_failure(self):
        token = None
        t = None
        my_obj = MyClass(token, t)
        self.assertNotEqual(my_obj.token, "my_token", "Token should not be equal to the arbitrary string 'my_token'")
        self.assertNotEqual(my_obj.t, 10, "t should not be equal to the arbitrary value 10")


if __name__ == "__main__":
    unittest.main()