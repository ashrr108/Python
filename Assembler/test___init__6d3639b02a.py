from __future__ import print_function
import sys
import unittest

class MyClass:
    def __init__(self, token, t):
        self.token = token
        self.t = t

class TestMyClass(unittest.TestCase):
    def test_init_valid(self):
        test_token = "test_token"
        test_t = 10
        my_class = MyClass(test_token, test_t)
        self.assertEqual(my_class.token, test_token)
        self.assertEqual(my_class.t, test_t)

    def test_init_invalid(self):
        test_token = None
        test_t = None
        my_class = MyClass(test_token, test_t)
        self.assertNotEqual(my_class.token, "valid_token")
        self.assertNotEqual(my_class.t, 5)

if __name__ == '__main__':
    unittest.main()