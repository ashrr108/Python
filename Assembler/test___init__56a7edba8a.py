
        pass


# class for represent a token
class Token:
     
         from __future__ import print_function
import sys

class Test__init__567aedba8(unittest.TestCase):
    
    def test_init_with_valid_data(self):
        token = Token("hello")
        self.assertEqual(token.value, "hello")

    def test_init_with_invalid_data(self):
        with self.assertRaises(TypeError):
            token = Token(123)

if __name__ == '__main__':
    unittest.main()