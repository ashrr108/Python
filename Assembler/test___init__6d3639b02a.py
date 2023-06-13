import unittest

class TokenTest(unittest.TestCase):

    def setUp(self):
        self.token = "example_token"
        self.t = 5

    def test_init(self):
        test_obj = TokenTestClass(self.token, self.t)
        self.assertEqual(test_obj.token, self.token)
        self.assertEqual(test_obj.t, self.t)

    def test_init_invalid_token(self):
        with self.assertRaises(TypeError):
            test_obj = TokenTestClass(None, self.t)

    def test_init_invalid_t(self):
        with self.assertRaises(TypeError):
            test_obj = TokenTestClass(self.token, "invalid_t")

class TokenTestClass:
    def __init__(self, token, t):
        if token is None or not isinstance(token, str):
            raise TypeError("Invalid token value")
        if not isinstance(t, int):
            raise TypeError("Invalid t value")

        self.token = token
        self.t = t

if __name__ == '__main__':
    unittest.main()