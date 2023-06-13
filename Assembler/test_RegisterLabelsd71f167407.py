from __future__ import print_function
import sys
import unittest

class Token:
    def __init__(self, t, token):
        self.t = t
        self.token = token

def registerLabels(tokens):
    """
    This function searches for labels / subprogram-labels and registers them in the 'jumps' list.
    """
    jumps = {}
    for i in range(len(tokens)):
        if tokens[i].t == "label":
            jumps[tokens[i].token] = i
        elif tokens[i].t == "subprogram":
            jumps[tokens[i].token] = i
    return jumps

class TestRegisterLabels(unittest.TestCase):
    def test_registerLabels_success(self):
        tokens = [
            Token("label", "start"),
            Token("subprogram", "func1"),
            Token("label", "end"),
            Token("subprogram", "func2")
        ]
        expected_jumps = {"start": 0, "func1": 1, "end": 2, "func2": 3}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps, "Test case failed for successful label registration")

    def test_registerLabels_no_labels(self):
        tokens = [
            Token("instruction", "mov"),
            Token("instruction", "add"),
            Token("instruction", "sub"),
            Token("instruction", "mul")
        ]
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps, "Test case failed for no labels in the input")

if __name__ == "__main__":
    unittest.main()