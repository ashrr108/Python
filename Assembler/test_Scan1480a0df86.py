from __future__ import print_function
import sys
import unittest

class InvalidSyntax(Exception):
    pass

def scanner(line):
    # TODO: Add the scanner implementation
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

class TestScan(unittest.TestCase):

    def setUp(self):
        global lines
        lines = []

    def test_scan_no_lines(self):
        with self.assertRaises(AssertionError) as context:
            scan()
        self.assertTrue("no lines" in str(context.exception))

    def test_scan_valid_lines(self):
        global lines
        lines = ["def foo():", "    print('Hello, world!')"]
        try:
            scan()
        except Exception as e:
            self.fail("scan() raised an unexpected exception: " + str(e))

    def test_scan_invalid_syntax(self):
        global lines
        lines = ["def foo():", "    print('Hello, world!')", "invalid line"]

        def scanner_with_invalid_syntax(line):
            if line == "invalid line":
                raise InvalidSyntax("Invalid syntax found")
            else:
                scanner(line)

        global scanner
        scanner = scanner_with_invalid_syntax

        with self.assertRaises(InvalidSyntax) as context:
            scan()
        self.assertTrue("Invalid syntax found" in str(context.exception))

if __name__ == "__main__":
    unittest.main()