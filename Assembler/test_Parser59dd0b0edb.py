from __future__ import print_function
import sys
import unittest

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

# Global variables
tokens = []
eax, ebx, ecx, edx = 0, 0, 0, 0
variables = {}
jumps = {}
stack = []
returnStack = []
zeroFlag = False

def parser():
    # ... (The provided parser function code goes here)

class TestParser(unittest.TestCase):
    def setUp(self):
        global tokens, eax, ebx, ecx, edx, variables, jumps, stack, returnStack, zeroFlag
        tokens = []
        eax, ebx, ecx, edx = 0, 0, 0, 0
        variables = {}
        jumps = {}
        stack = []
        returnStack = []
        zeroFlag = False

    def test_mov_register_value(self):
        global tokens, eax
        tokens = [Token("mov", ""), Token("eax", "register"), Token("5", "value")]
        parser()
        self.assertEqual(eax, 5)

    def test_mov_register_register(self):
        global tokens, eax, ebx
        tokens = [Token("mov", ""), Token("eax", "register"), Token("5", "value"),
                  Token("mov", ""), Token("ebx", "register"), Token("eax", "register")]
        parser()
        self.assertEqual(ebx, 5)

    def test_add_register_value(self):
        global tokens, eax
        tokens = [Token("mov", ""), Token("eax", "register"), Token("5", "value"),
                  Token("add", ""), Token("eax", "register"), Token("3", "value")]
        parser()
        self.assertEqual(eax, 8)

    def test_add_register_register(self):
        global tokens, eax, ebx
        tokens = [Token("mov", ""), Token("eax", "register"), Token("5", "value"),
                  Token("mov", ""), Token("ebx", "register"), Token("3", "value"),
                  Token("add", ""), Token("eax", "register"), Token("ebx", "register")]
        parser()
        self.assertEqual(eax, 8)

    # Add more test cases here for other commands and scenarios

if __name__ == '__main__':
    unittest.main()