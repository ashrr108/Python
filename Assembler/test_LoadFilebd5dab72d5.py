from __future__ import print_function
import sys
import unittest
import os
import tempfile

lines = []

def loadFile(fileName):
    """
    loadFile: This function loads the file and reads its lines.
    """
    global lines
    fo = open(fileName)
    for line in fo:
        lines.append(line)
    fo.close()

class TestLoadFile(unittest.TestCase):

    def test_loadFile_success(self):
        # Create a temporary file with some content
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(b"Line 1\nLine 2\nLine 3")
        temp_file.close()

        # Load the temporary file using loadFile function
        loadFile(temp_file.name)

        # Check if the lines are loaded correctly
        self.assertEqual(lines, ["Line 1\n", "Line 2\n", "Line 3"])

        # Clean up the temporary file
        os.unlink(temp_file.name)

    def test_loadFile_fileNotFound(self):
        # Attempt to load a non-existent file
        with self.assertRaises(FileNotFoundError):
            loadFile("non_existent_file.txt")

if __name__ == '__main__':
    unittest.main()