from __future__ import print_function
import sys
import unittest

class MyClass:
    def __init__(self, token, t):
        self.token = token
        self.t = t

class TestMyClass(unittest.TestCase):
    def test_init_valid(self):
        my_instance = MyClass("sample_token", 5)
        self.assertEqual(my_instance.token, "sample_token")
        self.assertEqual(my_instance.t, 5)

    def test_init_invalid(self):
        with self.assertRaises(TypeError):
            MyClass(123, "invalid_type")

if __name__ == '__main__':
    unittest.main()