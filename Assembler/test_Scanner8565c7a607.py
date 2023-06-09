from __future__ import print_function
import sys
import unittest


class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.value == other.value and self.token_type == other.token_type
        return False

    def __str__(self):
        return f"{self.token_type}: {self.value}"


class InvalidSyntax(Exception):
    pass


tokens = []


def scanner(string):
    global tokens
    # ... (rest of the scanner function code)


class TestScanner8565c7a607(unittest.TestCase):
    def test_valid_input(self):
        global tokens
        input_string = "mov eax, 1\nadd eax, 2\nsub eax, 1\n"
        expected_tokens = [
            Token("mov", "command"),
            Token("eax", "register"),
            Token("1", "value"),
            Token("add", "command"),
            Token("eax", "register"),
            Token("2", "value"),
            Token("sub", "command"),
            Token("eax", "register"),
            Token("1", "value"),
        ]
        scanner(input_string)
        self.assertEqual(tokens, expected_tokens)

    def test_invalid_input(self):
        global tokens
        input_string = "mov eax, 1\nadd ex, 2\nsub eax, 1\n"
        with self.assertRaises(InvalidSyntax):
            scanner(input_string)
       