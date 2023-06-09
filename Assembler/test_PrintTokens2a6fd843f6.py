from __future__ import print_function
import sys
import unittest

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

def printTokens(tokens):
    output = []
    for token in tokens:
        output.append(f"{token.token} --> {token.t}")
    return output

class TestPrintTokens(unittest.TestCase):
    
    def test_printTokens_empty_input(self):
        tokens = []
        expected_output = []
        self.assertEqual(printTokens(tokens), expected_output)

    def test_printTokens_valid_input(self):
        tokens = [
            Token("Hello", "Word"),
            Token("World", "Word"),
            Token("!", "Punctuation")
        ]
        expected_output = [
            "Hello --> Word",
            "World --> Word",
            "! --> Punctuation"
        ]
        self.assertEqual(printTokens(tokens), expected_output)

if __name__ == '__main__':
    unittest.main()