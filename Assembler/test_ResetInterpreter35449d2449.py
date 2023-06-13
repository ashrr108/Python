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
        self.eax, self.ebx, self.ecx, self.edx = 1, 2, 3, 4
        self.zeroFlag = True
        self.stack = [1, 2, 3]
        self.jumps = {"a": 1}
        self.variables = {"x": 1}
        self.lines = ["line1", "line2"]
        self.tokens = ["token1", "token2"]
        self.returnStack = [0]

    def TestResetInterpreter35449d2449(self):
        resetInterpreter()
        self.assertEqual(eax, 0, "eax should be reset to 0")
        self.assertEqual(ebx, 0, "ebx should be reset to 0")
        self.assertEqual(ecx, 0, "ecx should be reset to 0")
        self.assertEqual(edx, 0, "edx should be reset to 0")
        self.assertFalse(zeroFlag, "zeroFlag should be reset to False")
        self.assertEqual(stack, [], "stack should be reset to an empty list")
        self.assertEqual(jumps, {}, "jumps should be reset to an empty dictionary")
        self.assertEqual(variables, {}, "variables should be reset to an empty dictionary")
        self.assertEqual(lines, [], "lines should be reset to an empty list")
        self.assertEqual(tokens, [], "tokens should be reset to an empty list")
        self.assertEqual(returnStack, [], "returnStack should be reset to an empty list")

    def TestResetInterpreter35449d2449_after_changes(self):
        self.eax, self.ebx, self.ecx, self.edx = 5, 6, 7, 8
        self.zeroFlag = True
        self.stack = [4, 5, 6]
        self.jumps = {"b": 2}
        self.variables = {"y": 2}
        self.lines = ["line3", "line4"]
        self.tokens = ["token3", "token4"]
        self.returnStack = [1]

        resetInterpreter()
        self.assertEqual(eax, 0, "eax should be reset to 0")
        self.assertEqual(ebx, 0, "ebx should be reset to 0")
        self.assertEqual(ecx, 0, "ecx should be reset to 0")
        self.assertEqual(edx, 0, "edx should be reset to 0")
        self.assertFalse(zeroFlag, "zeroFlag should be reset to False")
        self.assertEqual(stack, [], "stack should be reset to an empty list")
        self.assertEqual(jumps, {}, "jumps should be reset to an empty dictionary")
        self.assertEqual(variables, {}, "variables should be reset to an empty dictionary")
        self.assertEqual(lines, [], "lines should be reset to an empty list")
        self.assertEqual(tokens, [], "tokens should be reset to an empty list")
        self.assertEqual(returnStack, [], "returnStack should be reset to an empty list")

if __name__ == "__main__":
    unittest.main()