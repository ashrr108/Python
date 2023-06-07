from __future__ import print_function
import sys


class Test__init__6d3639b02a(object):

    def test_token_is_set(self):
        token = 'test_token'
        t = 'test_t'
        obj = __init__(token, t)
        t.Log('token: %s' % obj.token)
        t.assertEqual(obj.token, token)

    def test_t_is_set(self):
        token = 'test_token'
        t = 'test_t'
        obj = __init__(token, t)
        t.Log('t: %s' % obj.t)
        t.assertEqual(obj.t, t)