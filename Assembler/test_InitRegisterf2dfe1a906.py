in range(9):
#         register.append(0)


 
         import unittest
from __future__ import print_function
import sys

class TestInitRegister2f1190a6(unittest.TestCase):
    def test_init_register_success(self):
        register = []
        InitRegister()
        self.assertEqual(len(register), 9)

    def test_init_register_failure(self):
        register = []
        InitRegister()
        self.assertEqual(len(register), 10)

if __name__ == '__main__':
    unittest.main()