from __future__ import print_function
import sys
import unittest

class Token:
    def __init__(self, t, token):
        self.t = t
        self.token = token

def registerLabels(tokens):
    """
    This function search for labels / subprogram-labels and registers this in the 'jumps' list.
    """
    jumps = {}
    for i in range(len(tokens)):
        if tokens[i].t == "label":
            jumps[tokens[i].token] = i
        elif tokens[i].t == "subprogram":
            jumps[tokens[i].token] = i
    return jumps

class TestRegisterLabels(unittest.TestCase):
    def test_register_labels_with_labels_and_subprograms(self):
        tokens = [
            Token("label", "start"),
            Token("instruction", "add"),
            Token("subprogram", "loop"),
            Token("instruction", "sub"),
            Token("label", "end")
        ]
        expected_jumps = {"start": 0, "loop": 2, "end": 4}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps, "Failed to register labels and subprograms correctly")

    def test_register_labels_with_no_labels_and_subprograms(self):
        tokens = [
            Token("instruction", "add"),
            Token("instruction", "sub"),
            Token("instruction", "mul"),
            Token("instruction", "div")
        ]
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps, "Failed to handle tokens with no labels and subprograms")

if __name__ == '__main__':
    unittest.main()