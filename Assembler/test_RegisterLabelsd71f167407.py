from __future__ import print_function
import sys
import unittest

class Token:
    def __init__(self, t, token):
        self.t = t
        self.token = token

def registerLabels(tokens, jumps):
    """
    This function search for labels / subprogram-labels and registers this in the 'jumps' list.
    """
    for i in range(len(tokens)):
        if tokens[i].t == "label":
            jumps[tokens[i].token] = i
        elif tokens[i].t == "subprogram":
            jumps[tokens[i].token] = i

class TestRegisterLabels(unittest.TestCase):
    def test_registerLabels_success(self):
        tokens = [Token("label", "start"), Token("subprogram", "sub1"), Token("label", "end")]
        jumps = {}
        registerLabels(tokens, jumps)
        expected_jumps = {"start": 0, "sub1": 1, "end": 2}
        self.assertEqual(jumps, expected_jumps, "registerLabels should register labels and subprograms correctly")

    def test_registerLabels_no_labels(self):
        tokens = [Token("instruction", "load"), Token("instruction", "store"), Token("instruction", "jump")]
        jumps = {}
        registerLabels(tokens, jumps)
        expected_jumps = {}
        self.assertEqual(jumps, expected_jumps, "registerLabels should not register any labels if none are present")

if __name__ == '__main__':
    unittest.main()