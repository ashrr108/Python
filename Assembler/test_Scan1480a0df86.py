from __future__ import print_function
import sys
import unittest


class InvalidSyntax(Exception):
    pass


def scanner(line):
    # Dummy scanner function for testing purposes
    if "invalid" in line:
        raise InvalidSyntax("Invalid syntax found in line")
    return True


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

    def test_scan_valid_lines(self):
        global lines
        lines = ["valid line 1", "valid line 2", "valid line 3"]
        try:
            scan()
        except Exception as e:
            self.fail(f"scan() raised {e.__class__.__name__} unexpectedly")

    def test_scan_invalid_lines(self):
        global lines
        lines = ["valid line 1", "invalid line 2", "valid line 3"]
        with self.assertRaises(InvalidSyntax):
            scan()


if __name__ == "__main__":
    unittest.main()