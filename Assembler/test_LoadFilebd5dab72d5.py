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

class TestLoadFile(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("Line 1\nLine 2\nLine 3")

    def tearDown(self):
        os.remove(self.test_file)

    def test_loadFile_success(self):
        loadFile(self.test_file)
        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0], "Line 1\n")
        self.assertEqual(lines[1], "Line 2\n")
        self.assertEqual(lines[2], "Line 3")

    def test_loadFile_fileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            loadFile("non_existent_file.txt")

if __name__ == "__main__":
    unittest.main()