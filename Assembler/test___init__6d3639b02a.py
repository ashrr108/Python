from __future__ import print_function
import sys
import unittest

class MyClass:
    def __init__(self, token, t):
        self.token = token
        self.t = t

class TestMyClass(unittest.TestCase):
    def test_init_valid(self):
        my_object = MyClass("example_token", 5)
        self.assertEqual(my_object.token, "example_token")
        self.assertEqual(my_object.t, 5)

    def test_init_invalid_token(self):
        with self.assertRaises(TypeError):
            MyClass(123, 5)

    def test_init_invalid_t(self):
        with self.assertRaises(TypeError):
            MyClass("example_token", "invalid_t")

if __name__ == '__main__':
    unittest.main()