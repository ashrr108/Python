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
        self.eax = 1
        self.ebx = 2
        self.ecx = 3
        self.edx = 4
        self.zeroFlag = True
        self.stack = [1, 2, 3]
        self.jumps = {"jump1": 5}
        self.variables = {"var1": 10}
        self.lines = ["line1", "line2"]
        self.tokens = ["token1", "token2"]
        self.returnStack = [5, 6]

    def test_reset_interpreter_success(self):
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

    def test_reset_interpreter_failure(self):
        self.assertNotEqual(eax, self.eax)
        self.assertNotEqual(ebx, self.ebx)
        self.assertNotEqual(ecx, self.ecx)
        self.assertNotEqual(edx, self.edx)
        self.assertNotEqual(zeroFlag, self.zeroFlag)
        self.assertNotEqual(stack, self.stack)
        self.assertNotEqual(jumps, self.jumps)
        self.assertNotEqual(variables, self.variables)
        self.assertNotEqual(lines, self.lines)
        self.assertNotEqual(tokens, self.tokens)
        self.assertNotEqual(returnStack, self.returnStack)

if __name__ == '__main__':
    unittest.main()