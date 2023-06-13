from __future__ import print_function
import sys
import unittest

class InvalidSyntax(Exception):
    pass

class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.type = token_type

tokens = []

def scanner(string):
    # (The original scanner function code goes here)

class TestScanner8565c7a607(unittest.TestCase):
    def test_valid_input(self):
        global tokens
        tokens = []
        input_string = 'mov eax, 1\nadd ebx, 2\nsub ecx, 3\nint 0x80'
        expected_tokens = [
            Token('mov', 'command'),
            Token('eax', 'register'),
            Token('1', 'value'),
            Token('add', 'command'),
            Token('ebx', 'register'),
            Token('2', 'value'),
            Token('sub', 'command'),
            Token('ecx', 'register'),
            Token('3', 'value'),
            Token('int', 'command'),
            Token('0x80', 'value')
        ]
        scanner(input_string)
        self.assertEqual(len(tokens), len(expected_tokens))
        for i in range(len(tokens)):
            self.assertEqual(tokens[i].value, expected_tokens[i].value)
            self.assertEqual(tokens[i].type, expected_tokens[i].type)

    def test_invalid_input(self):
        global tokens
        tokens = []
        input_string = 'mov eaz, 1\nadd ebx, 2\nsub ecx, 3\nint 0x80'
