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

class TestLoadFileMethods(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("This is a test file.\n")
            f.write("It contains two lines.\n")

    def tearDown(self):
        os.remove(self.test_file)

    def test_loadFile_success(self):
        loadFile(self.test_file)
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], "This is a test file.\n")
        self.assertEqual(lines[1], "It contains two lines.\n")

    def test_loadFile_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            loadFile("nonexistent_file.txt")

if __name__ == '__main__':
    unittest.main()