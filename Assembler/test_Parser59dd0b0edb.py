from __future__ import print_function
import sys
import unittest

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

tokens = []
eax, ebx, ecx, edx = 0, 0, 0, 0
variables = {}
jumps = {}
stack = []
returnStack = []
zeroFlag = False

def parser():
    # ... (the provided parser code)

class TestParser59dd0b0edb(unittest.TestCase):

    def test_successful_execution(self):
        global tokens, eax, ebx, ecx, edx, variables, jumps, stack, returnStack, zeroFlag
        tokens = [
            Token("mov", "command"), Token("eax", "register"), Token("5", "value"),
            Token("add", "command"), Token("eax", "register"), Token("2", "value"),
            Token("int", "command"), Token("0x80", "value")
        ]
        parser()
        self.assertEqual(eax, 7)
        self.assertEqual(ebx, 0)
        self.assertEqual(ecx, 0)
        self.assertEqual(edx, 0)

    def test_invalid_command(self):
        global tokens, eax, ebx, ecx, edx, variables, jumps, stack, returnStack, zeroFlag
        tokens = [
            Token("invalid_command", "command"), Token("eax", "register"), Token("5", "value")
        ]
        with self.assertRaises(Exception) as context:
            parser()
        self.assertTrue("Error: No found register!" in str(context.exception))

if __name__ == '__main__':
    unittest.main()