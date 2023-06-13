from __future__ import print_function
import sys
import os
import unittest

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

class TestLoadFileMethods(unittest.TestCase):

    def test_loadFile_success(self):
        test_file = "test_file.txt"
        with open(test_file, "w") as f:
            f.write("Line 1\nLine 2\nLine 3")

        loadFile(test_file)
        self.assertEqual(lines, ["Line 1\n", "Line 2\n", "Line 3"])

        os.remove(test_file)

    def test_loadFile_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            loadFile("nonexistent_file.txt")

if __name__ == '__main__':
    unittest.main()