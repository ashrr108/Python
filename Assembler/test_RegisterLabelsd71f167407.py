from __future__ import print_function
import sys
import unittest

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
        tokens = [
            {"t": "label", "token": "start"},
            {"t": "subprogram", "token": "calc"},
            {"t": "label", "token": "end"}
        ]
        expected_jumps = {
            "start": 0,
            "calc": 1,
            "end": 2
        }
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)

    def test_registerLabels_no_labels(self):
        tokens = [
            {"t": "instruction", "token": "mov"},
            {"t": "instruction", "token": "add"},
            {"t": "instruction", "token": "sub"}
        ]
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)

    def test_registerLabels_mixed_tokens(self):
        tokens = [
            {"t": "label", "token": "start"},
            {"t": "instruction", "token": "mov"},
            {"t": "subprogram", "token": "calc"},
            {"t": "instruction", "token": "add"},
            {"t": "label", "token": "end"},
            {"t": "instruction", "token": "sub"}
        ]
        expected_jumps = {
            "start": 0,
            "calc": 2,
            "end": 4
        }
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)

if __name__ == "__main__":
    unittest.main()