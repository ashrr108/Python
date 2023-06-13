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
        result.append("{} --> {}".format(token.token, token.t))
    return result

class TestPrintTokens(unittest.TestCase):

    def test_printTokens_with_valid_input(self):
        tokens = [Token("hello", "word"), Token("123", "number"), Token("!", "punctuation")]
        expected_output = ["hello --> word", "123 --> number", "! --> punctuation"]
        self.assertEqual(printTokens(tokens), expected_output)

    def test_printTokens_with_empty_input(self):
        tokens = []
        expected_output = []
        self.assertEqual(printTokens(tokens), expected_output)

if __name__ == "__main__":
    unittest.main()