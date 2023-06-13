from __future__ import print_function
import sys
import unittest

class InvalidSyntax(Exception):
    pass

def scanner(line):
    # TODO: Implement the scanner function
    pass

def scan(lines):
    """
    scan: applies function scanner() to each line of the source code.
    """
    assert len(lines) > 0, "no lines"
    for line in lines:
        try:
            scanner(line)
        except InvalidSyntax:
            print("line=", line)

class TestScan(unittest.TestCase):

    def test_scan_valid_code(self):
        lines = ["def foo():", "    print('Hello, world!')", "foo()"]
        try:
            scan(lines)
        except Exception as e:
            self.fail(f"scan() raised {type(e).__name__} unexpectedly")

    def test_scan_invalid_code(self):
        lines = ["def foo():", "    print('Hello, world!')", "foo)("]
        with self.assertRaises(InvalidSyntax):
            scan(lines)

if __name__ == "__main__":
    unittest.main()