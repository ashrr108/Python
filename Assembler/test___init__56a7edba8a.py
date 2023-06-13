import unittest

# class for representing a token
class Token:
    def __init__(self, value):
        self.value = value

class TestToken(unittest.TestCase):
    def test_init(self):
        token = Token("example")
        self.assertEqual(token.value, "example", "Token value should be 'example'")

    def test_init_empty(self):
        token = Token("")
        self.assertEqual(token.value, "", "Token value should be an empty string")

if __name__ == '__main__':
    unittest.main()