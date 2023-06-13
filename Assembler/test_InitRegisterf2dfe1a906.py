from __future__ import print_function
import sys


def initRegister():
    register = []
    for i in range(9):
        register.append(0)


class TestInitRegisterf2dfe1a906(unittest.TestCase):

    def test_initRegister_1(self):
        register = []
        initRegister()
        self.assertEqual(register, [0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_initRegister_2(self):
        register = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        initRegister()
        self.assertEqual(register, [0, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()