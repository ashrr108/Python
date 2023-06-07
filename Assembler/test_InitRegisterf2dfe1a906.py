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
        self.assertEqual(result, expected, "The initRegister function should initialize a list with 9 zeros.")

    def test_initRegister_length(self):
        result = initRegister()
        self.assertEqual(len(result), 9, "The initRegister function should create a list with a length of 9.")

if __name__ == '__main__':
    unittest.main()