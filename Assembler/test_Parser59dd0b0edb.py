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
    global tokens
    global eax, ebx, ecx, edx

    assert len(tokens) > 0, "no tokens"

    pointer = 0
    token = Token("", "")
    tmpToken = Token("", "")

    while pointer < len(tokens):

        token = tokens[pointer]

        # ... (rest of the parser code)

        pointer += 1

class TestParser59dd0b0edb(unittest.TestCase):

    def test_basic_mov_and_add(self):
        global tokens, eax, ebx
        tokens = [Token("mov", "command"), Token("eax", "register"), Token("5", "value"),
                  Token("mov", "command"), Token("ebx", "register"), Token("3", "value"),
                  Token("add", "command"), Token("eax", "register"), Token("ebx", "register")]
        parser()
        self.assertEqual(eax, 8)
        self.assertEqual(ebx, 3)

    def test_invalid_command(self):
        global tokens
        tokens = [Token("invalid_command", "command"), Token("eax", "register"), Token("5", "value")]
        with self.assertRaises(AssertionError):
            parser()

if __name__ == '__main__':
    unittest.main()