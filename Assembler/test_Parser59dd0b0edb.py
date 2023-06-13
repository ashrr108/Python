from __future__ import print_function
import sys

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

def TestParser59dd0b0edb():
    global tokens
    global eax, ebx, ecx, edx

    # Test case 1: Test mov command with registers
    tokens = [Token("mov", "command"), Token("eax", "register"), Token("ebx", "register")]
    eax = 5
    ebx = 10
    parser()
    assert eax == 10, "Test case 1 failed: eax should be 10, but got {}".format(eax)
    print("Test case 1 passed")

    # Test case 2: Test add command with registers
    tokens = [Token("add", "command"), Token("eax", "register"), Token("ebx", "register")]
    eax = 5
    ebx = 10
    parser()
    assert eax == 15, "Test case 2 failed: eax should be 15, but got {}".format(eax)
    print("Test case 2 passed")

if __name__ == "__main__":
    TestParser59dd0b0edb()