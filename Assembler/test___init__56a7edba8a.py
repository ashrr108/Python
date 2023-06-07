from __future__ import print_function
import sys


class Test__init__56a7edba8a(object):

    def test_token_init_with_type_and_value(self):
        token = Token("IDENTIFIER", "test")
        t.Log("token: %s" % token)
        t.AssertEqual(token.type, "IDENTIFIER")
        t.AssertEqual(token.value, "test")

    def test_token_init_with_type_and_value_and_line_number(self):
        token = Token("IDENTIFIER", "test", 10)
        t.Log("token: %s" % token)
        t.AssertEqual(token.type, "IDENTIFIER")
        t.AssertEqual(token.value, "test")
        t.AssertEqual(token.line_number, 10)