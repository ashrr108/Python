from __future__ import print_function
import sys
import unittest


class InvalidSyntax(Exception):
    pass


def scanner(line):
    # TODO: Implement the scanner function here
    pass


lines = []


def scan():
    """
    scan: applys function scanner() to each line of the source code.
    """
    global lines
    assert len(lines) > 0, "no lines"
    for line in lines:
        try:
            scanner(line)
        except InvalidSyntax:
            print("line=", line)


class TestScanMethods(unittest.TestCase):

    def test_scan_valid_input(self):
        global lines
        lines = ["def test():", "    pass"]
        try:
            scan()
        except AssertionError as e:
            self.fail("scan() raised AssertionError unexpectedly: " + str(e))

    def test_scan_invalid_input(self):
        global lines
        lines = ["def test()::", "    pass"]
        with self.assertRaises(InvalidSyntax):
            scan()


if __name__ == '__main__':
    unittest.main()