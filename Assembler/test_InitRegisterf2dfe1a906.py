from __future__ import print_function
import sys
import unittest

def initRegister():
    register = []
    for i in range(9):
        register.append(0)
    return register

class TestInitRegister(unittest.TestCase):

    def test_init_register_length(self):
        register = initRegister()
        self.assertEqual(len(register), 9, "Length of register should be 9")

    def test_init_register_values(self):
        register = initRegister()
        for value in register:
            self.assertEqual(value, 0, "All values in register should be 0")

if __name__ == '__main__':
    unittest.main()