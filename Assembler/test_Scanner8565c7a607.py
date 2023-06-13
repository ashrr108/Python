from __future__ import print_function
import sys
import unittest

class InvalidSyntax(Exception):
    pass

class Token:
    def __init__(self, value, type):
        self.value = value
        self.type = type

tokens = []

def scanner(string):
    # ... (the provided scanner function)

class TestScanner8565c7a607(unittest.TestCase):

    def test_valid_input(self):
        global tokens
        tokens = []
        input_string = 'mov eax, 0\nadd eax, 5\nsub eax, 3\nint 0x80'
        expected_tokens = [
            Token('mov', 'command'), Token('eax', 'register'), Token('0', 'value'),
            Token('add', 'command'), Token('eax', 'register'), Token('5', 'value'),
            Token('sub', 'command'), Token('eax', 'register'), Token('3', 'value'),
            Token('int', 'command'), Token('0x80', 'value')
        ]

        scanner(input_string)
        self.assertEqual(len(tokens), len(expected_tokens))

        for i, token in enumerate(tokens):
            self.assertEqual(token.value, expected_tokens[i].value)
            self.assertEqual(token.type, expected_tokens[i].type)

    def test_invalid_input(self):
        global tokens
        tokens = []
        input_string = 'mov eaz, 0\nadd eax, 5\nsub eax, 3\nint 0x80'

        with self.assertRaises(InvalidSyntax):
            scanner(input_string)

if