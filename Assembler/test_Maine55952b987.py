from __future__ import print_function
import sys
import unittest
import io
import contextlib

def main():
    """
    reads textfiles from the command-line and interprets them.
    """

    # [1:] because the first argument is the program itself.
    for arg in sys.argv[1:]:

        resetInterpreter()  # resets interpreter mind

        try:

            loadFile(arg)
            scan()
            registerLabels()
            parser()

        except Exception as e:

            print(f"Error: {e}")

def resetInterpreter():
    pass

def loadFile(arg):
    pass

def scan():
    pass

def registerLabels():
    pass

def parser():
    pass

class TestMaine55952b987(unittest.TestCase):

    def test_main_success(self):
        test_args = ["testfile.txt"]
        with open("testfile.txt", "w") as f:
            f.write("This is a test file.")

        with contextlib.redirect_stdout(io.StringIO()) as f:
            sys.argv[1:] = test_args
            main()
        output = f.getvalue()
        self.assertNotIn("Error:", output)

    def test_main_file_not_found(self):
        test_args = ["non_existent_file.txt"]
        with contextlib.redirect_stdout(io.StringIO()) as f:
            sys.argv[1:] = test_args
            main()
        output = f.getvalue()
        self.assertIn("Error:", output)

if __name__ == "__main__":
    unittest.main()