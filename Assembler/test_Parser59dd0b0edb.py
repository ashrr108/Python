from __future__ import print_function
import sys

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

eax, ebx, ecx, edx = 0, 0, 0, 0
tokens = []
variables = {}
stack = []
jumps = {}
returnStack = []
zeroFlag = False

def TestParser59dd0b0edb():
    global tokens, eax, ebx, ecx, edx, variables, stack, jumps, returnStack, zeroFlag

    # Test case 1: Simple mov and add operations
    tokens = [
        Token("mov", "command"),
        Token("eax", "register"),
        Token("10", "value"),
        Token("mov", "command"),
        Token("ebx", "register"),
        Token("20", "value"),
        Token("add", "command"),
        Token("eax", "register"),
        Token("ebx", "register"),
        Token("int", "command"),
        Token("0x80", "value")
    ]
    parser()
    assert eax == 30, "Test case 1 failed: eax should be 30"
    assert ebx == 20, "Test case 1 failed: ebx should be 20"
    print("Test case 1 passed")

    # Reset global variables
    eax, ebx, ecx, edx = 0, 0, 0, 0
    tokens = []
    variables = {}
    stack = []
    jumps = {}
    returnStack = []
    zeroFlag = False

    # Test case 2: Testing push, pop, and jmp operations
    tokens = [
        Token("mov", "command"),
        Token("eax", "register"),
        Token("5", "value"),
        Token("push", "command"),
        Token("eax", "register"),
        Token("mov", "eax", "register"),
        Token("10", "value"),
        Token("pop", "command"),
        Token("ebx", "register"),
        Token("label1", "label"),
        Token("add", "command"),
        Token("eax", "register"),
        Token("ebx", "register"),
        Token("cmp", "command"),
        Token("eax", "register"),
        Token("15", "value"),
        Token("je", "command"),
        Token("label2", "label"),
        Token("jmp", "command"),
        Token("label1", "label"),
        Token("label2", "label"),
        Token("int", "command"),
        Token("0x80", "value")
    ]
    parser()
    assert eax == 15, "Test case 2 failed: eax should be 15"
    assert ebx == 5, "Test case 2 failed: ebx should be 5"
    print("Test case 2 passed")

TestParser59dd0b0edb()