from __future__ import print_function
import sys
import unittest

class InvalidSyntax(Exception):
    pass

def scanner(line):
    # TODO: Implement the scanner function logic here
    pass

def scan(lines):
    """
    scan: applys function scanner() to each line of the source code.
    """
    assert len(lines) > 0, "no lines"
    for line in lines:
        try:
            scanner(line)
        except InvalidSyntax:
            print("line=", line)

class TestScan1480a0df86(unittest.TestCase):

    def test_scan_valid_input(self):
        lines = [
            "def hello():",
            "    print('Hello, world!')",
            "hello()"
        ]

        try:
            scan(lines)
        except Exception as e:
            self.fail(f"scan() raised {type(e)} unexpectedly")

    def test_scan_invalid_syntax(self):
        lines = [
            "def hello():",
            "    print('Hello, world!')",
            "    invalid_syntax_line"
        ]

        with self.assertRaises(InvalidSyntax):
            scan(lines)

if __name__ == '__main__':
    unittest.main()