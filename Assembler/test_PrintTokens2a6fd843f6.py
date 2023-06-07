token, " --> ", token.t)


# main program
 
         import unittest
	from __future__ import print_function
import sys

class TestPrintTokens2648fd36(unittest.TestCase):
    def test_print_tokens_success(self):
        tokens = ['a', 'b', 'c']
        printTokens(tokens)
        self.assertEqual(sys.stdout.getvalue(), 'a --> a\nb --> b\nc --> c\n')

    def test_print_tokens_empty(self):
        tokens = []
        printTokens(tokens)
        self.assertEqual(sys.stdout.getvalue(), '')

if __name__ == '__main__':
    unittest.main()