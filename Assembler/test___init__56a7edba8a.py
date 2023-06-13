from __future__ import print_function
import sys
import unittest

# class for representing a token
class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

class TestToken(unittest.TestCase):
    def test_token_creation(self):
        token = Token("test_value", "test_type")
        self.assertEqual(token.value, "test_value")
        self.assertEqual(token.token_type, "test_type")

    def test_token_creation_with_empty_values(self):
        token = Token("", "")
        self.assertEqual(token.value, "")
        self.assertEqual(token.token_type, "")

if __name__ == "__main__":
    unittest.main()