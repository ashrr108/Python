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
            {'t': 'instruction', 'token': 'LOAD'},
            {'t': 'subprogram', 'token': 'sub1'},
            {'t': 'instruction', 'token': 'ADD'},
            {'t': 'label', 'token': 'end'},
        ]
        expected_jumps = {'start': 0, 'sub1': 2, 'end': 4}
        self.assertEqual(registerLabels(tokens), expected_jumps)

    def test_registerLabels_no_labels(self):
        tokens = [
            {'t': 'instruction', 'token': 'LOAD'},
            {'t': 'instruction', 'token': 'ADD'},
            {'t': 'instruction', 'token': 'STORE'},
        ]
        expected_jumps = {}
        self.assertEqual(registerLabels(tokens), expected_jumps)

if __name__ == '__main__':
    unittest.main()