from __future__ import print_function
import sys
import unittest

def initRegister():
    register = []
    for i in range(9):
        register.append(0)
    return register

class TestInitRegister(unittest.TestCase):

    def test_initRegister_all_zeros(self):
        register = initRegister()
        self.assertEqual(register, [0, 0, 0, 0, 0, 0, 0, 0, 0], "The register should be initialized with all zeros")

    def test_initRegister_length(self):
        register = initRegister()
        self.assertEqual(len(register), 9, "The register should have a length of 9")

if __name__ == '__main__':
    unittest.main()