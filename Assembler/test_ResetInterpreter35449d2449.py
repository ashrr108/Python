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

class TestInterpreterReset(unittest.TestCase):

    def setUp(self):
        resetInterpreter()

    def TestResetInterpreter35449d2449(self):
        resetInterpreter()
        self.assertEqual(eax, 0, "eax should be 0 after reset")
        self.assertEqual(ebx, 0, "ebx should be 0 after reset")
        self.assertEqual(ecx, 0, "ecx should be 0 after reset")
        self.assertEqual(edx, 0, "edx should be 0 after reset")
        self.assertEqual(zeroFlag, False, "zeroFlag should be False after reset")
        self.assertEqual(stack, [], "stack should be empty after reset")
        self.assertEqual(jumps, {}, "jumps should be empty after reset")
        self.assertEqual(variables, {}, "variables should be empty after reset")
        self.assertEqual(lines, [], "lines should be empty after reset")
        self.assertEqual(tokens, [], "tokens should be empty after reset")
        self.assertEqual(returnStack, [], "returnStack should be empty after reset")

    def TestResetInterpreterStateChange(self):
        global eax, ebx, ecx, edx, zeroFlag, stack
        global variables, jumps, lines, tokens, returnStack

        eax = 1
        ebx = 2
        ecx = 3
        edx = 4
        zeroFlag = True
        stack = [1, 2, 3]
        jumps = {"test": 1}
        variables = {"a": 1}
        lines = ["line1", "line2"]
        tokens = ["token1", "token2"]
        returnStack = [1]

        resetInterpreter()

        self.assertEqual(eax, 0, "eax should be 0 after reset")
        self.assertEqual(ebx, 0, "ebx should be 0 after reset")
        self.assertEqual(ecx, 0, "ecx should be 0 after reset")
        self.assertEqual(edx, 0, "edx should be 0 after reset")
        self.assertEqual(zeroFlag, False, "zeroFlag should be False after reset")
        self.assertEqual(stack, [], "stack should be empty after reset")
        self.assertEqual(jumps, {}, "jumps should be empty after reset")
        self.assertEqual(variables, {}, "variables should be empty after reset")
        self.assertEqual(lines, [], "lines should be empty after reset")
        self.assertEqual(tokens, [], "tokens should be empty after reset")
        self.assertEqual(returnStack, [], "returnStack should be empty after reset")

if __name__ == '__main__':
    unittest.main()