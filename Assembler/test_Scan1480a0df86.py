from __future__ import print_function
import sys
import unittest

# TODO: Define the scanner function and InvalidSyntax exception here, as they are used in the scan function.

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

    def test_scan_success(self):
        global lines
        lines = ["print('Hello, world!')", "x = 5", "y = x + 3"]
        try:
            scan()
        except Exception as e:
            self.fail("scan() raised an unexpected exception: " + str(e))

    def test_scan_failure(self):
        global lines
        lines = ["print('Hello, world!')", "x = 5", "y = x + 3", "invalid line"]
        with self.assertRaises(InvalidSyntax):
            scan()

    def test_scan_empty_input(self):
        global lines
        lines = []
        with self.assertRaises(AssertionError) as context:
            scan()
        self.assertEqual(str(context.exception), "no lines")

if __name__ == "__main__":
    unittest.main()