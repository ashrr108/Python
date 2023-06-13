from __future__ import print_function
import sys
import unittest

def resetInterpreter():
    """
    resets the interpreter mind.
    """
    global eax, ebx, ecx, edx, zeroFlag, stack
    global variables, jumps, lines, tokens, returnStack
    eax = 0
    ebx = 0
    ecx = 0
    edx = 0
    zeroFlag = False
    stack = []
    jumps = {}
    variables = {}
    lines = []
    tokens = []
    returnStack = []

class TestResetInterpreter(unittest.TestCase):

    def setUp(self):
        self.eax = 5
        self.ebx = 6
        self.ecx = 7
        self.edx = 8
        self.zeroFlag = True
        self.stack = [1, 2, 3]
        self.jumps = {"label": 5}
        self.variables = {"x": 10}
        self.lines = ["line1", "line2"]
        self.tokens = ["token1", "token2"]
        self.returnStack = [4, 5]

    def TestResetInterpreter35449d2449(self):
        resetInterpreter()
        self.assertEqual(eax, 0)
        self.assertEqual(ebx, 0)
        self.assertEqual(ecx, 0)
        self.assertEqual(edx, 0)
        self.assertFalse(zeroFlag)
        self.assertEqual(stack, [])
        self.assertEqual(jumps, {})
        self.assertEqual(variables, {})
        self.assertEqual(lines, [])
        self.assertEqual(tokens, [])
        self.assertEqual(returnStack, [])

    def TestResetInterpreterEdgeCase(self):
        self.stack = [1] * 100000
        self.returnStack = [4] * 100000
        resetInterpreter()
        self.assertEqual(eax, 0)
        self.assertEqual(ebx, 0)
        self.assertEqual(ecx, 0)
        self.assertEqual(edx, 0)
        self.assertFalse(zeroFlag)
        self.assertEqual(stack, [])
        self.assertEqual(jumps, {})
        self.assertEqual(variables, {})
        self.assertEqual(lines, [])
        self.assertEqual(tokens, [])
        self.assertEqual(returnStack, [])

if __name__ == "__main__":
    unittest.main()