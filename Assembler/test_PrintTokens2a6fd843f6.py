from __future__ import print_function
import sys
import unittest


# Method to be tested
def print_tokens(tokens):
    token_list = []
    for token in tokens:
        token_list.append((token.token, token.t))
    return token_list


# Test class
class TestPrintTokens(unittest.TestCase):

    # Test case 1: Test with a valid list of tokens
    def test_valid_tokens(self):
        class Token:
            def __init__(self, token, t):
                self.token = token
                self.t = t

        tokens = [Token("token1", "type1"), Token("token2", "type2"), Token("token3", "type3")]
        expected_output = [("token1", "type1"), ("token2", "type2"), ("token3", "type3")]

        result = print_tokens(tokens)
        self.assertEqual(result, expected_output, "The output should match the expected token list.")

    # Test case 2: Test with an empty list of tokens
    def test_empty_tokens(self):
        tokens = []
        expected_output = []

        result = print_tokens(tokens)
        self.assertEqual(result, expected_output, "The output should be an empty list.")


# Main program
if __name__ == '__main__':
    unittest.main()