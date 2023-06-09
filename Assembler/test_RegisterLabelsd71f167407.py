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

    def test_register_labels_d71f167407(self):
        tokens = [
            {"t": "label", "token": "start"},
            {"t": "instruction", "token": "load"},
            {"t": "subprogram", "token": "sub1"},
            {"t": "label", "token": "end"},
        ]
        expected_jumps = {
            "start": 0,
            "sub1": 2,
            "end": 3,
        }
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps, "Failed to register labels and subprograms correctly")

    def test_register_labels_no_labels(self):
        tokens = [
            {"t": "instruction", "token": "load"},
            {"t": "instruction", "token": "store"},
            {"t": "instruction", "token": "add"},
        ]
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps, "Failed to handle tokens with no labels or subprograms")

if __name__ == "__main__":
    unittest.main()