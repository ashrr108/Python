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
variables = {}
stack = []
returnStack = []
jumps = {}
zeroFlag = False

class TestParser59dd0b0edb(unittest.TestCase):
    
    def setUp(self):
        global tokens, eax, ebx, ecx, edx, variables, stack, returnStack, jumps, zeroFlag
        tokens = []
        eax, ebx, ecx, edx = 0, 0, 0, 0
        variables = {}
        stack = []
        returnStack = []
        jumps = {}
        zeroFlag = False

    def test_mov_register(self):
        global tokens
        tokens = [Token("mov", ""), Token("eax", "register"), Token("10", "")]
        parser()
        self.assertEqual(eax, 10)

    def test_mov_register_to_register(self):
        global tokens
        tokens = [Token("mov", ""), Token("eax", "register"), Token("10", ""), Token("mov", ""), Token("ebx", "register"), Token("eax", "register")]
        parser()
        self.assertEqual(ebx, 10)

    def test_add_register(self):
        global tokens
        tokens = [Token("mov", ""), Token("eax", "register"), Token("5", ""), Token("add", ""), Token("eax", "register"), Token("10", "")]
        parser()
        self.assertEqual(eax, 15)

    def test_sub_register(self):
        global tokens
        tokens = [Token("mov", ""), Token("eax", "register"), Token("10", ""), Token("sub", ""), Token("eax", "register"), Token("5", "")]
        parser()
        self.assertEqual(eax, 5)

    def test_error_handling(self):
        global tokens
        tokens = [Token("mov", ""), Token("eax", "register")]
        with self.assertRaises(SystemExit) as cm:
            parser()
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)