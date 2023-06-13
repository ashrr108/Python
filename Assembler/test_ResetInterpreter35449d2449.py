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
        global eax, ebx, ecx, edx, zeroFlag, stack
        global variables, jumps, lines, tokens, returnStack
        eax = 5
        ebx = 6
        ecx = 7
        edx = 8
        zeroFlag = True
        stack = [1, 2, 3]
        jumps = {'label': 1}
        variables = {'var1': 10}
        lines = ['line1', 'line2']
        tokens = ['token1', 'token2']
        returnStack = [4, 5, 6]

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
        global eax, ebx, ecx, edx, zeroFlag, stack
        global variables, jumps, lines, tokens, returnStack
        eax = sys.maxsize
        ebx = sys.maxsize
        ecx = sys.maxsize
        edx = sys.maxsize
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

if __name__ == '__main__':
    unittest.main()