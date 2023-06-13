import unittest

# class for representing a token
class Token:
    def __init__(self, value):
        self.value = value

# Test cases for Token class
class TestToken(unittest.TestCase):
    def test_init(self):
        token = Token("example")
        self.assertEqual(token.value, "example")

    def test_init_empty(self):
        token = Token("")
        self.assertEqual(token.value, "")

    def test_init_none(self):
        token = Token(None)
        self.assertIsNone(token.value)

# Run the tests
if __name__ == '__main__':
    unittest.main()