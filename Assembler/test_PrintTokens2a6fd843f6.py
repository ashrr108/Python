from __future__ import print_function
import sys
import unittest

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

def printTokens(tokens):
    result = []
    for token in tokens:
        result.append(f"{token.token} --> {token.t}")
    return result

class TestPrintTokens(unittest.TestCase):
    def test_printTokens_with_valid_input(self):
        tokens = [Token("token1", "type1"), Token("token2", "type2"), Token("token3", "type3")]
        expected_result = ["token1 --> type1", "token2 --> type2", "token3 --> type3"]
        self.assertEqual(printTokens(tokens), expected_result)

    def test_printTokens_with_empty_input(self):
        tokens = []
        expected_result = []
        self.assertEqual(printTokens(tokens), expected_result)

if __name__ == "__main__":
    unittest.main()