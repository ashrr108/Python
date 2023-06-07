.token = token
        self.t = t


#  
         import unittest
from __future__ import print_function
import sys

class Test__init__63396b20(unittest.TestCase):
    def test_init_success(self):
        token = "1234567890"
        t = 10
        obj = Test__init__(token, t)
        self.assertEqual(obj.token, token)
        self.assertEqual(obj.t, t)

    def test_init_failure(self):
        token = "1234567890"
        t = -10
        with self.assertRaises(ValueError):
            obj = Test__init__(token, t)

if __name__ == '__main__':
    unittest.main()