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

class TestScan1480a0df86(unittest.TestCase):

    def test_scan_valid_code(self):
        valid_code = ["def foo():", "    print('Hello, World!')", "foo()"]
        try:
            scan(valid_code)
        except InvalidSyntax:
            self.fail("scan() raised InvalidSyntax for valid code")

    def test_scan_invalid_code(self):
        invalid_code = ["def foo()::", "    print('Hello, World!')", "foo()"]
        with self.assertRaises(InvalidSyntax):
            scan(invalid_code)

if __name__ == '__main__':
    unittest.main()