from __future__ import print_function
import sys
import unittest
from io import StringIO

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

tokens = []
eax, ebx, ecx, edx = 0, 0, 0, 0
stack = []
jumps = {}
returnStack = []
variables = {}
zeroFlag = False

class TestParser(unittest.TestCase):

    def setUp(self):
        global tokens, eax, ebx, ecx, edx, stack, jumps, returnStack, variables, zeroFlag
        tokens = []
        eax, ebx, ecx, edx = 0, 0, 0, 0
        stack = []
        jumps = {}
        returnStack = []
        variables = {}
        zeroFlag = False

    def test_mov_command(self):
        global tokens
        tokens = [Token("mov", "command"), Token("eax", "register"), Token("5", "value")]
        parser()
        self.assertEqual(eax, 5)

    def test_add_command(self):
        global tokens, eax
        tokens = [Token("mov", "command"), Token("eax", "register"), Token("5", "value"),
                  Token("add", "command"), Token("eax", "register"), Token("3", "value")]
        parser()
        self.assertEqual(eax, 8)

    def test_sub_command(self):
        global tokens, eax
        tokens = [Token("mov", "command"), Token("eax", "register"), Token("5", "value"),
                  Token("sub", "command"), Token("eax", "register"), Token("3", "value")]
        parser()
        self.assertEqual(eax, 2)

    def test_mul_command(self):
        global tokens, eax
        tokens = [Token("mov", "command"), Token("eax", "register"), Token("5", "value"),
                  Token("mul", "command"), Token("eax", "register")]
        parser()
        self.assertEqual(eax, 25)

    def test_div_command(self):
        global tokens, eax
        tokens = [Token("mov", "command"), Token("eax", "register"), Token("25", "value"),
                  Token("div", "command"), Token("eax", "register")]
        parser()
        self.assertEqual(eax, 1)

    def test_push_pop_command(self):
        global tokens, eax, stack
        tokens = [Token("mov", "command"), Token("eax", "register"), Token("5", "value"),
                  Token("push", "command"), Token("eax", "register"),
                  Token("pop", "command"), Token("ebx", "register")]
        parser()
        self.assertEqual(eax, 5)
        self.assertEqual(ebx, 5)

if __name__ == '__main__':
    unittest.main()