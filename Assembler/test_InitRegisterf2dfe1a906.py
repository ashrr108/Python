from __future__ import print_function
import sys
import unittest

def initRegister():
    register = []
    for i in range(9):
        register.append(0)
    return register

class TestInitRegister(unittest.TestCase):

    def test_init_register_success(self):
        result = initRegister()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result, expected, "Initialization of register failed")

    def test_init_register_length(self):
        result = initRegister()
        expected_length = 9
        self.assertEqual(len(result), expected_length, "Register length is incorrect")

if __name__ == "__main__":
    unittest.main()