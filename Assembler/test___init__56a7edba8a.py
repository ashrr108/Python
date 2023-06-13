from __future__ import print_function
import sys


class Test__init__56a7edba8a(unittest.TestCase):

    def test_token_init(self):
        token = Token()
        self.assertEqual(token.type, None)
        self.assertEqual(token.value, None)

    def test_token_init_with_type_and_value(self):
        token = Token("NUMBER", "123")
        self.assertEqual(token.type, "NUMBER")
        self.assertEqual(token.value, "123")