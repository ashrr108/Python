from __future__ import print_function
import sys
import unittest


class Test__init__56a7edba8a(unittest.TestCase):

    def test_token_is_not_none(self):
        token = "1234567890"
        t = "test"
        instance = __init__(token, t)
        assert instance.token == token

    def test_token_is_none(self):
        token = None
        t = "test"
        with self.assertRaises(TypeError):
            __init__(token, t)


if __name__ == "__main__":
    unittest.main()