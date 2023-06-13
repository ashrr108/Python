import unittest

# class for representing a token
class Token:
    def __init__(self, value):
        self.value = value

# Test cases for Token class
class TestToken(unittest.TestCase):

    def test_init_valid(self):
        token = Token("test_value")
        self.assertEqual(token.value, "test_value", "Token initialization with valid value should set the value attribute correctly.")

    def test_init_invalid(self):
        with self.assertRaises(TypeError, msg="Token initialization with non-string value should raise a TypeError."):
            Token(42)

if __name__ == "__main__":
    unittest.main()