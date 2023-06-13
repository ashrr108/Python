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

    def setUp(self):
        self.test_file = "test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("This is a test file.\n")
            f.write("This is the second line.\n")

    def tearDown(self):
        os.remove(self.test_file)

    def test_loadFile_success(self):
        loadFile(self.test_file)
        self.assertEqual(lines, ["This is a test file.\n", "This is the second line.\n"])

    def test_loadFile_fileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            loadFile("non_existent_file.txt")

if __name__ == "__main__":
    unittest.main()