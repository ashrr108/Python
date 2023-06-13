from __future__ import print_function
import sys
import unittest


def loadFile(filename):
    """
    loadFile: This function loads the file and returns the lines in the file.
    Args:
        filename: The file name to be loaded.
    """
    global lines
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line.strip())


class TestLoadFilebd5dab72d5(unittest.TestCase):
    """
    TestLoadFilebd5dab72d5: This test case is to test loadFile method.
    """

    def test_loadFile(self):
        """
        test_loadFile: This test case is to test loadFile method.
        """
        global lines
        lines = []
        loadFile("test.txt")
        self.Log("lines: ", lines)
        self.AssertEqual(lines, ["This is line 1", "This is line 2", "This is line 3"])

    def test_loadFileWithInvalidFileNamebd5dab72d5(self):
        """
        test_loadFileWithInvalidFileNamebd5dab72d5: This test case is to test loadFile method with invalid file name.
        """
        global lines
        lines = []
        try:
            loadFile("invalid.txt")
        except Exception as e:
            self.Log("Exception: ", e)
            self.AssertEqual(e.message, "File not found")
        else:
            self.Error("Exception not thrown")


if __name__ == "__main__":
    t = unittest.TestLoader().loadTestsFromTestCase(TestLoadFilebd5dab72d5)
    unittest.TextTestRunner(verbosity=2).run(t)