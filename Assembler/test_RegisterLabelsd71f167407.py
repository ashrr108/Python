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

    def test_registerLabels_success(self):
        tokens = [Token("label", "start"), Token("subprogram", "sub1"), Token("label", "end")]
        expected_jumps = {"start": 0, "sub1": 1, "end": 2}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps, "registerLabels did not return expected jumps")

    def test_registerLabels_no_labels(self):
        tokens = [Token("instruction", "instr1"), Token("instruction", "instr2"), Token("instruction", "instr3")]
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps, "registerLabels should return empty jumps when no labels or subprograms are present")

if __name__ == "__main__":
    unittest.main()