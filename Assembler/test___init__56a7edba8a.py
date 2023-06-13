from __future__ import print_function
import sys
import unittest

# class for represent a token
class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

class TestTokenMethods(unittest.TestCase):
    def test_token_initialization(self):
        token = Token("123", "integer")
        self.assertEqual(token.value, "123")
        self.assertEqual(token.token_type, "integer")

    def test_token_initialization_invalid_type(self):
        with self.assertRaises(TypeError):
            token = Token(123, "integer")

if __name__ == '__main__':
    unittest.main()