from __future__ import print_function
import sys
import unittest

class MyClass:
    def __init__(self, token, t):
        self.token = token
        self.t = t

class TestMyClass(unittest.TestCase):

    def test_init_valid_input(self):
        my_object = MyClass("test_token", 42)
        self.assertEqual(my_object.token, "test_token", "Token should be 'test_token'")
        self.assertEqual(my_object.t, 42, "t should be 42")

    def test_init_invalid_input(self):
        with self.assertRaises(TypeError):
            my_object = MyClass(None, 42)

        with self.assertRaises(TypeError):
            my_object = MyClass("test_token", None)

if __name__ == '__main__':
    unittest.main()