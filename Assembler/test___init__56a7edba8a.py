import unittest

# class for represent a token
class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

class TestTokenMethods(unittest.TestCase):

    def test_token_initialization(self):
        token = Token("TestValue", "TestType")
        self.assertEqual(token.value, "TestValue")
        self.assertEqual(token.token_type, "TestType")

    def test_token_initialization_with_empty_values(self):
        token = Token("", "")
        self.assertEqual(token.value, "")
        self.assertEqual(token.token_type, "")

if __name__ == '__main__':
    unittest.main()