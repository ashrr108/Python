from __future__ import print_function
import sys

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

tokens = []
eax, ebx, ecx, edx = 0, 0, 0, 0
stack = []
jumps = {}
returnStack = []
variables = {}
zeroFlag = False

def TestParser59dd0b0edb():
    global tokens, eax, ebx, ecx, edx, stack, jumps, returnStack, variables, zeroFlag

    # Test case 1: mov, add, and sub commands
    tokens = [
        Token("mov", "mov"), Token("eax", "register"), Token("10", "value"),
        Token("add", "add"), Token("eax", "register"), Token("5", "value"),
        Token("sub", "sub"), Token("eax", "register"), Token("3", "value"),
    ]
    parser()
    assert eax == 12, "Test case 1 failed: eax should be 12"
    print("Test case 1 passed")

    # Reset global variables
    eax, ebx, ecx, edx = 0, 0, 0, 0
    stack = []
    jumps = {}
    returnStack = []
    variables = {}
    zeroFlag = False

    # Test case 2: push, pop, and jmp commands
    tokens = [
        Token("mov", "mov"), Token("eax", "register"), Token("5", "value"),
        Token("push", "push"), Token("eax", "register"),
        Token("mov", "mov"), Token("ebx", "register"), Token("10", "value"),
        Token("pop", "pop"), Token("ecx", "register"),
        Token("label1", "label"),
        Token("sub", "sub"), Token("ebx", "register"), Token("1", "value"),
        Token("cmp", "cmp"), Token("ebx", "register"), Token("eax", "register"),
        Token("je", "je"), Token("label2", "label"),
        Token("jmp", "jmp"), Token("label1", "label"),
        Token("label2", "label")
    ]
    parser()
    assert eax == 5, "Test case 2 failed: eax should be 5"
    assert ebx == 5, "Test case 2 failed: ebx should be 5"
    assert ecx == 5, "Test case 2 failed: ecx should be 5"
    print("Test case 2 passed")

TestParser59dd0b0edb()