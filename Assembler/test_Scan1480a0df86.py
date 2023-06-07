       except InvalidSyntax:
            print("line=", line)


 
         import sys
from __future__ import print_function

def scan():
    """
    scan: apply function scanner() to each line of the source code.
    """
    global lines
    assert len(lines) > 0, "no lines"
    for line in lines:
        try:
            scanner(line)
        except InvalidSyntax:
            print("line=", line)


class TestScan4800df68(unittest.TestCase):

    def test_scan_valid_code(self):
        lines = ["#include <stdio.h>", "int main() {", "    return 0;", "}"]
        scan()

    def test_scan_invalid_code(self):
        lines = ["#include <stdio.h>", "int main() {", "    return 0;", "}"]
        with self.assertRaises(InvalidSyntax):
            scan()