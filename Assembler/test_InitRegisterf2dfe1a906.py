from __future__ import print_function
import sys


def initRegister():
    global register
    for i in range(9):
        register.append(0)


class TestInitRegisterf2dfe1a906(unittest.TestCase):

    def testInitRegister(self):
        register = []
        initRegister()
        self.assertEqual(len(register), 9)
        for i in range(9):
            self.assertEqual(register[i], 0)


if __name__ == '__main__':
    unittest.main()