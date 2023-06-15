from __future__ import print_function
import sys
import unittest

# Method to be tested
def printTokens(tokens):
    result = []
    for token in tokens:
        result.append(f"{token.token} --> {token.t}")
    return result

# Test case class
class TestPrintTokens(unittest.TestCase):

    # Test case 1: Check if the method works with valid input
    def test_printTokens_valid_input(self):
        class Token:
            def __init__(self, token, t):
                self.token = token
                self.t = t

        tokens = [Token("hello", "word"), Token("42", "number"), Token(";", "punctuation")]
        expected_output = ["hello --> word", "42 --> number", "; --> punctuation"]
        actual_output = printTokens(tokens)

        self.assertEqual(actual_output, expected_output, "The method did not return the expected output for valid input.")

    # Test case 2: Check if the method works with an empty list
    def test_printTokens_empty_list(self):
        tokens = []
        expected_output = []
        actual_output = printTokens(tokens)

        self.assertEqual(actual_output, expected_output, "The method did not return the expected output for an empty list.")
        
# Run the test suite
if __name__ == "__main__":
    unittest.main()