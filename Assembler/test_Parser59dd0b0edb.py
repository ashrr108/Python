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
stack = []
jumps = {}
variables = {}
returnStack = []
zeroFlag = False

def parser():
    # ... (Same parser code provided in the prompt)

class TestParser(unittest.TestCase):
    def setUp(self):
        global tokens, eax, ebx, ecx, edx, stack, jumps, variables, returnStack, zeroFlag
        tokens = []
        eax, ebx, ecx, edx = 0, 0, 0, 0
        stack = []
        jumps = {}
        variables = {}
        returnStack = []
        zeroFlag = False

    def TestParser59dd0b0edb(self):
        global tokens
        tokens = [Token("mov", "command"), Token("eax", "register"), Token("10", "value"),
                  Token("add", "command"), Token("eax", "register"), Token("5", "value")]
        parser()
        self.assertEqual(eax, 15, "Failed to add value to eax")

        tokens = [Token("mov", "eax", "register"), Token("10", "value"),
                  Token("mov", "ebx", "register"), Token("eax", "register"),
                  Token("add", "ebx", "register"), Token("5", "value")]
        parser()
        self.assertEqual(ebx, 15, "Failed to move eax value to ebx and add value to ebx")

    def test_parser_zero_flag(self):
        global tokens, zeroFlag
        tokens = [Token("mov", "eax", "register"), Token("10", "value"),
                  Token("mov", "ebx", "register"), Token("10", "value"),
                  Token("cmp", "command"), Token("eax", "register"), Token("ebx", "register")]
        parser()
        self.assertTrue(zeroFlag, "Failed to set zero flag when eax and ebx are equal")

        tokens = [Token("mov", "eax", "register"), Token("10", "value"),
                  Token("mov", "ebx", "register"), Token("5", "value"),
                  Token("cmp", "command"), Token("eax", "register"), Token("ebx", "register")]
        parser()
        self.assertFalse(zeroFlag, "Failed to unset zero flag when eax and ebx are not equal")

if __name__ == "__main__":
    unittest.main()