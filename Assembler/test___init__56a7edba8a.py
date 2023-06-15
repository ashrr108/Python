import unittest

class Token:
    def __init__(self, value):
        self.value = value

class TestToken(unittest.TestCase):
    def test_init_valid(self):
        token = Token(5)
        self.assertEqual(token.value, 5, "Token value should be 5")

    def test_init_invalid(self):
        with self.assertRaises(TypeError):
            token = Token(None)

if __name__ == '__main__':
    unittest.main()
```