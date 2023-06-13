from __future__ import print_function
import sys
import unittest

# Method to be tested
def printTokens(tokens):
    result = []
    for token in tokens:
        output = "{} --> {}".format(token.token, token.t)
        result.append(output)
        print(output)
    return result

# Test class
class TestPrintTokens(unittest.TestCase):
    def test_printTokens_with_valid_data(self):
        class MockToken:
            def __init__(self, token, t):
                self.token = token
                self.t = t

        tokens = [
            MockToken("token1", "t1"),
            MockToken("token2", "t2"),
            MockToken("token3", "t3")
        ]

        expected_output = [
            "token1 --> t1",
            "token2 --> t2",
            "token3 --> t3"
        ]

        result = printTokens(tokens)
        self.assertEqual(result, expected_output)

    def test_printTokens_with_empty_list(self):
        tokens = []
        expected_output = []

        result = printTokens(tokens)
        self.assertEqual(result, expected_output)

# main program
if __name__ == '__main__':
    unittest.main()