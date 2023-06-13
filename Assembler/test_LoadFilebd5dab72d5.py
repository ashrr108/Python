from __future__ import print_function
import sys
import unittest
import os

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
        with open("temp_file.txt", "w") as temp_file:
            temp_file.write("Line 1\nLine 2\nLine 3")

        # Call the loadFile function
        loadFile("temp_file.txt")

        # Check if the lines are loaded correctly
        self.assertEqual(lines, ["Line 1\n", "Line 2\n", "Line 3"])

        # Remove the temporary file
        os.remove("temp_file.txt")

    def test_loadFile_fileNotFound(self):
        # Call the loadFile function with a non-existing file
        with self.assertRaises(FileNotFoundError):
            loadFile("non_existent_file.txt")

if __name__ == '__main__':
    unittest.main()