import unittest

def print_tokens(tokens):
    output = []
    for token in tokens:
        output.append(f"{token.token} --> {token.t}")
    return output

class Token:
    def __init__(self, token, t):
        self.token = token
        self.t = t

class TestPrintTokens(unittest.TestCase):

    def test_print_tokens_success(self):
        tokens = [Token("token1", "t1"), Token("token2", "t2"), Token("token3", "t3")]
        expected_output = ["token1 --> t1", "token2 --> t2", "token3 --> t3"]
        self.assertEqual(print_tokens(tokens), expected_output)

    def test_print_tokens_empty_list(self):
        tokens = []
        expected_output = []
        self.assertEqual(print_tokens(tokens), expected_output)

    def test_print_tokens_invalid_input(self):
        tokens = "invalid_input"
        with self.assertRaises(TypeError):
            print_tokens(tokens)

if __name__ == '__main__':
    unittest.main()