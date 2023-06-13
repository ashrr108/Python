from __future__ import print_function
import sys


class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type


class InvalidSyntax(Exception):
    pass


tokens = []


def scanner(string):
    # ... (The original scanner function code goes here)


def TestScanner8565c7a607():
    global tokens

    # Test case 1: Valid input
    try:
        tokens = []
        input_string = "mov eax, 1\nadd eax, 2\nsub eax, 1"
        expected_tokens = [
            Token("mov", "command"),
            Token("eax", "register"),
            Token("1", "value"),
            Token("add", "command"),
            Token("eax", "register"),
            Token("2", "value"),
            Token("sub", "command"),
            Token("eax", "register"),
            Token("1", "value"),
        ]
        scanner(input_string)
        for i, token in enumerate(tokens):
            assert (
                token.value == expected_tokens[i].value
                and token.token_type == expected_tokens[i].token_type
            ), f"Test case 1 failed: expected {expected_tokens[i].value}, got {token.value}"
        print("Test case 1 passed")

    except Exception as e:
        print("Test case 1 failed:", e)

    # Test case 2: Invalid input
    try:
        tokens = []
        input_string = "mov eaz