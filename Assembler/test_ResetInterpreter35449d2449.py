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
        jumps = {"label": 10}
        variables = {"x": 1, "y": 2}
        lines = ["line1", "line2"]
        tokens = ["token1", "token2"]
        returnStack = [20, 30]

    def test_resetInterpreter_success(self):
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

    def test_resetInterpreter_failure(self):
        resetInterpreter()

        self.assertNotEqual(eax, 5)
        self.assertNotEqual(ebx, 6)
        self.assertNotEqual(ecx, 7)
        self.assertNotEqual(edx, 8)
        self.assertNotEqual(zeroFlag, True)
        self.assertNotEqual(stack, [1, 2, 3])
        self.assertNotEqual(jumps, {"label": 10})
        self.assertNotEqual(variables, {"x": 1, "y": 2})
        self.assertNotEqual(lines, ["line1", "line2"])
        self.assertNotEqual(tokens, ["token1", "token2"])
        self.assertNotEqual(returnStack, [20, 30])


if __name__ == '__main__':
    unittest.main()