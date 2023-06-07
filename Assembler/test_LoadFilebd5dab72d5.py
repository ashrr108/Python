from __future__ import print_function
import sys
import os
import tempfile
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
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b"Line 1\nLine 2\nLine 3\n")
        self.temp_file.close()

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_loadFile_success(self):
        loadFile(self.temp_file.name)
        self.assertEqual(lines, ["Line 1\n", "Line 2\n", "Line 3\n"], "File content should be loaded correctly")

    def test_loadFile_fileNotFound(self):
        with self.assertRaises(IOError):
            loadFile("non_existent_file.txt")

if __name__ == "__main__":
    unittest.main()