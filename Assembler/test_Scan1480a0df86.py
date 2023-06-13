from __future__ import print_function
import sys
import unittest

class InvalidSyntax(Exception):
    pass

def scanner(line):
    # TODO: Implement the actual scanner function here
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

class TestScan1480a0df86(unittest.TestCase):

    def test_scan_valid_input(self):
        global lines
        lines = ["valid line 1", "valid line 2"]
        try:
            scan()
        except Exception as e:
            self.fail(f"scan() raised an unexpected exception: {e}")

    def test_scan_invalid_input(self):
        global lines
        lines = ["valid line 1", "invalid line", "valid line 2"]

        with self.assertRaises(InvalidSyntax):
            scan()

    def test_scan_empty_input(self):
        global lines
        lines = []

        with self.assertRaises(AssertionError):
            scan()

if __name__ == '__main__':
    unittest.main()