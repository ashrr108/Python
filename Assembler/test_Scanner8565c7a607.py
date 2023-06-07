from __future__ import print_function
import sys
import unittest

class InvalidSyntax(Exception):
    pass

class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

    def __eq__(self, other):
        return self.value == other.value and self.token_type == other.token_type

tokens = []

def scanner(string):
    # ... (scanner function code here) ...

class TestScanner8565c7a607(unittest.TestCase):

    def test_valid_input(self):
        global tokens
        tokens = []
        input_string = "mov eax, 1"
        expected_tokens = [
            Token("mov", "command"),
            Token("eax", "register"),
            Token("1", "value")
        ]
        scanner(input_string)
        self.assertEqual(tokens, expected_tokens)

    def test_invalid_input(self):
        global tokens
        tokens = []
        input_string = "invalid_command eax, 1"
        with self.assertRaises(InvalidSyntax):
            scanner(input_string)

if __name__ == '__main__':
    unittest.main()