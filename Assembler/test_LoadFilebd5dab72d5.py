import unittest
from io import StringIO
from unittest.mock import patch
from tempfile import NamedTemporaryFile

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
        global lines
        lines.clear()
        with NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write("Line 1\n")
            temp_file.write("Line 2\n")
            temp_file.write("Line 3\n")
            temp_file.flush()

        loadFile(temp_file.name)

        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0], "Line 1\n")
        self.assertEqual(lines[1], "Line 2\n")
        self.assertEqual(lines[2], "Line 3\n")

    def test_loadFile_fileNotFound(self):
        global lines
        lines.clear()
        with self.assertRaises(FileNotFoundError):
            loadFile("non_existent_file.txt")

        self.assertEqual(len(lines), 0)

if __name__ == "__main__":
    unittest.main()