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
        self.eax = 10
        self.ebx = 20
        self.ecx = 30
        self.edx = 40
        self.zeroFlag = True
        self.stack = [1, 2, 3]
        self.jumps = {'label': 5}
        self.variables = {'x': 10, 'y': 20}
        self.lines = ['line1', 'line2']
        self.tokens = ['token1', 'token2']
        self.returnStack = [1, 2]

    def TestResetInterpreter35449d2449(self):
        resetInterpreter()
        self.assertEqual(self.eax, 0)
        self.assertEqual(self.ebx, 0)
        self.assertEqual(self.ecx, 0)
        self.assertEqual(self.edx, 0)
        self.assertFalse(self.zeroFlag)
        self.assertEqual(self.stack, [])
        self.assertEqual(self.jumps, {})
        self.assertEqual(self.variables, {})
        self.assertEqual(self.lines, [])
        self.assertEqual(self.tokens, [])
        self.assertEqual(self.returnStack, [])

    def TestResetInterpreterAfterOperations(self):
        self.eax = 5
        self.stack.append(4)
        self.jumps['new_label'] = 10
        self.variables['z'] = 30
        self.lines.append('line3')
        self.tokens.append('token3')
        self.returnStack.append(3)

        resetInterpreter()

        self.assertEqual(self.eax, 0)
        self.assertEqual(self.ebx, 0)
        self.assertEqual(self.ecx, 0)
        self.assertEqual(self.edx, 0)
        self.assertFalse(self.zeroFlag)
        self.assertEqual(self.stack, [])
        self.assertEqual(self.jumps, {})
        self.assertEqual(self.variables, {})
        self.assertEqual(self.lines, [])
        self.assertEqual(self.tokens, [])
        self.assertEqual(self.returnStack, [])

if __name__ == '__main__':
    unittest.main()