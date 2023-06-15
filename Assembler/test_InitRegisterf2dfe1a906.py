from __future__ import print_function
import sys
import unittest

def initRegister():
    register = []
    for i in range(9):
        register.append(0)
    return register

class TestInitRegister(unittest.TestCase):

    def test_initRegister_length(self):
        result = initRegister()
        self.assertEqual(len(result), 9, "Length of register should be 9")

    def test_initRegister_values(self):
        result = initRegister()
        for value in result:
            self.assertEqual(value, 0, "All values in register should be initialized to 0")

if __name__ == '__main__':
    unittest.main()