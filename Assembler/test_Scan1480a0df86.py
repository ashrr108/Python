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

class TestScan(unittest.TestCase):

    def setUp(self):
        global lines
        lines = []

    def test_scan_success(self):
        global lines
        lines = ["line1", "line2", "line3"]
        try:
            scan()
        except Exception as e:
            self.fail("scan() raised an exception: " + str(e))

    def test_scan_no_lines(self):
        global lines
        lines = []
        with self.assertRaises(AssertionError, msg="no lines"):
            scan()

    def test_scan_invalid_syntax(self):
        global lines
        lines = ["line1", "line2", "line3"]

        def scanner_with_invalid_syntax(line):
            if line == "line2":
                raise InvalidSyntax

        global scanner
        scanner = scanner_with_invalid_syntax

        with self.assertRaises(InvalidSyntax):
            scan()

if __name__ == '__main__':
    unittest.main()