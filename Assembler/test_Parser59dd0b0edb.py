from __future__ import print_function
import sys

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

def TestParser59dd0b0edb():
    global tokens, eax, ebx, ecx, edx, variables, stack, zeroFlag, jumps, returnStack

    # Test case 1: Simple addition operation
    tokens = [
        Token("mov", "mov"), Token("eax", "register"), Token("5", "value"),
        Token("add", "add"), Token("eax", "register"), Token("3", "value"),
    ]
    eax, ebx, ecx, edx = 0, 0, 0, 0
    variables = {}
    stack = []
    zeroFlag = False
    jumps = {}
    returnStack = []
    parser()
    assert eax == 8, "Test case 1 failed: eax should be 8, got {}".format(eax)
    print("Test case 1 passed")

    # Test case 2: Simple subtraction operation
    tokens = [
        Token("mov", "mov"), Token("ebx", "register"), Token("10", "value"),
        Token("sub", "sub"), Token("ebx", "register"), Token("4", "value"),
    ]
    eax, ebx, ecx, edx = 0, 0, 0, 0
    variables = {}
    stack = []
    zeroFlag = False
    jumps = {}
    returnStack = []
    parser()
    assert ebx == 6, "Test case 2 failed: ebx should be 6, got {}".format(ebx)
    print("Test case 2 passed")

TestParser59dd0b0edb()