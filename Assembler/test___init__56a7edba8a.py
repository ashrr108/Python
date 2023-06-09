import unittest

class Token:
    def __init__(self, value):
        self.value = value

class TestToken(unittest.TestCase):

    def test_init_valid_value(self):
        token = Token("test_value")
        self.assertEqual(token.value, "test_value", "Token value should be 'test_value'")

    def test_init_empty_value(self):
        token = Token("")
        self.assertEqual(token.value, "", "Token value should be an empty string")

    def test_init_none_value(self):
        token = Token(None)
        self.assertIsNone(token.value, "Token value should be None")

if __name__ == "__main__":
    unittest.main()