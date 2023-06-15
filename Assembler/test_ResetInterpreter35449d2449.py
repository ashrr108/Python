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

    def test_initial_state(self):
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

    def test_reset_after_changes(self):
        global eax, ebx, ecx, edx, zeroFlag, stack
        global variables, jumps, lines, tokens, returnStack
        
        eax = 1
        ebx = 2
        ecx = 3
        edx = 4
        zeroFlag = True
        stack = [1, 2, 3]
        jumps = {'label': 10}
        variables = {'a': 1, 'b': 2}
        lines = ['line1', 'line2']
        tokens = ['token1', 'token2']
        returnStack = [1, 2]

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