from __future__ import print_function
import sys
import unittest

class MyClass:
    def __init__(self, token, t):
        self.token = token
        self.t = t

class TestMyClass(unittest.TestCase):

    def test_init_valid(self):
        my_obj = MyClass("test_token", 5)
        self.assertEqual(my_obj.token, "test_token")
        self.assertEqual(my_obj.t, 5)

    def test_init_invalid(self):
        with self.assertRaises(TypeError):
            my_obj = MyClass(None, "invalid_t")

if __name__ == '__main__':
    unittest.main()