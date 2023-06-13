from __future__ import print_function
import sys
import unittest

def initRegister():
    register = []
    for i in range(9):
        register.append(0)
    return register

class TestInitRegister(unittest.TestCase):

    def test_initRegister_success(self):
        result = initRegister()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result, expected, "The register should be initialized with all 0s.")

    def test_initRegister_length(self):
        result = initRegister()
        expected_length = 9
        self.assertEqual(len(result), expected_length, "The register should have a length of 9.")

if __name__ == '__main__':
    unittest.main()