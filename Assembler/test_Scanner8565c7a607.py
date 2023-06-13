from __future__ import print_function
import sys
import unittest

class InvalidSyntax(Exception):
    pass

class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

tokens = []

def scanner(string):
    # (The given scanner function)

class TestScanner8565c7a607(unittest.TestCase):

    def test_valid_input(self):
        global tokens
        tokens = []
        input_string = 'mov eax, 1\nadd edx, 2\nsub eax, edx\nint 0x80\n'
        scanner(input_string)
        self.assertEqual(len(tokens), 12)
        self.assertEqual(tokens[0].value, 'mov')
        self.assertEqual(tokens[0].token_type, 'command')
        self.assertEqual(tokens[1].value, 'eax')
        self.assertEqual(tokens[1].token_type, 'register')
        self.assertEqual(tokens[2].value, ',')
        self.assertEqual(tokens[3].value, '1')
        self.assertEqual(tokens[3].token_type, 'value')

    def test_invalid_input(self):
        global tokens
        tokens = []
        input_string = 'mov eax, 1\nadd edx, 2\nsub eax, edx\nint 0x80\ninvalid_command\n'
        with self.assertRaises(InvalidSyntax):
            scanner(input_string)

if __name__ == '__main__':
    unittest.main()