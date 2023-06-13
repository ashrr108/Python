from __future__ import print_function
import sys
import unittest

# Method to be tested
def print_tokens(tokens):
    result = []
    for token in tokens:
        result.append(f"{token.token} --> {token.t}")
    return result

# Test case class
class TestPrintTokens(unittest.TestCase):

    # Test case 1: Normal scenario
    def test_normal_scenario(self):
        class Token:
            def __init__(self, token, t):
                self.token = token
                self.t = t

        tokens = [Token("token1", "t1"), Token("token2", "t2"), Token("token3", "t3")]
        expected_output = ["token1 --> t1", "token2 --> t2", "token3 --> t3"]

        self.assertEqual(print_tokens(tokens), expected_output)

    # Test case 2: Empty input
    def test_empty_input(self):
        tokens = []
        expected_output = []

        self.assertEqual(print_tokens(tokens), expected_output)

    # Test case 3: Invalid input (not a list of tokens)
    def test_invalid_input(self):
        tokens = "invalid_input"
        with self.assertRaises(TypeError):
            print_tokens(tokens)

# Main program
if __name__ == "__main__":
    unittest.main()