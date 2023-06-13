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
            {'t': 'label', 'token': 'start'},
            {'t': 'subprogram', 'token': 'sub1'},
            {'t': 'label', 'token': 'end'},
            {'t': 'subprogram', 'token': 'sub2'}
        ]
        expected_jumps = {
            'start': 0,
            'sub1': 1,
            'end': 2,
            'sub2': 3
        }
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)

    def test_registerLabels_empty(self):
        tokens = []
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)

    def test_registerLabels_no_labels(self):
        tokens = [
            {'t': 'instruction', 'token': 'mov'},
            {'t': 'instruction', 'token': 'add'},
            {'t': 'instruction', 'token': 'sub'}
        ]
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)

if __name__ == '__main__':
    unittest.main()