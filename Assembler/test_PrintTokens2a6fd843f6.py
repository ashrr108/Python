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
    def test_printTokens_normal_case(self):
        tokens = [
            Token("token1", "type1"),
            Token("token2", "type2"),
            Token("token3", "type3")
        ]
        
        expected_output = [
            "token1 --> type1",
            "token2 --> type2",
            "token3 --> type3"
        ]
        
        self.assertEqual(printTokens(tokens), expected_output)

    def test_printTokens_empty_list(self):
        tokens = []
        expected_output = []
        self.assertEqual(printTokens(tokens), expected_output)

    def test_printTokens_single_token(self):
        tokens = [Token("token1", "type1")]
        expected_output = ["token1 --> type1"]
        self.assertEqual(printTokens(tokens), expected_output)

    def test_printTokens_duplicate_tokens(self):
        tokens = [
            Token("token1", "type1"),
            Token("token1", "type1"),
            Token("token2", "type2")
        ]
        
        expected_output = [
            "token1 --> type1",
            "token1 --> type1",
            "token2 --> type2"
        ]
        
        self.assertEqual(printTokens(tokens), expected_output)

# main program
if __name__ == '__main__':
    unittest.main()