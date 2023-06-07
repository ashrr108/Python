from __future__ import print_function
import sys
import unittest

# Original function to be tested
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


# Test class
class TestRegisterLabels(unittest.TestCase):

    def test_registerLabels_valid_labels(self):
        tokens = [
            {'t': 'label', 'token': 'LABEL1'},
            {'t': 'subprogram', 'token': 'SUB1'},
            {'t': 'label', 'token': 'LABEL2'},
        ]
        expected_jumps = {
            'LABEL1': 0,
            'SUB1': 1,
            'LABEL2': 2,
        }
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)

    def test_registerLabels_no_labels(self):
        tokens = [
            {'t': 'operation', 'token': 'ADD'},
            {'t': 'operation', 'token': 'SUB'},
            {'t': 'operation', 'token': 'MUL'},
        ]
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)

    def test_registerLabels_empty_tokens(self):
        tokens = []
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)

    def test_registerLabels_invalid_token_type(self):
        tokens = [
            {'t': 'invalid', 'token': 'INVALID1'},
            {'t': 'invalid', 'token': 'INVALID2'},
        ]
        expected_jumps = {}
        result = registerLabels(tokens)
        self.assertEqual(result, expected_jumps)


if __name__ == '__main__':
    unittest.main()