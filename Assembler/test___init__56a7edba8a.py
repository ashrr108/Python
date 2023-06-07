import unittest

class Token:
    def __init__(self, value):
        self.value = value

class TestTokenMethods(unittest.TestCase):
    def test_token_initialization(self):
        token = Token("example")
        self.assertEqual(token.value, "example", "Token value should be 'example'")

    def test_token_initialization_empty_string(self):
        token = Token("")
        self.assertEqual(token.value, "", "Token value should be an empty string")

if __name__ == '__main__':
    unittest.main()