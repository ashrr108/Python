from __future__ import print_function
import sys
import unittest

def loadFile(fileName):
    """
    loadFile: This function loads the file and reads its lines.
    """
    global lines
    fo = open(fileName)
    for line in fo:
        lines.append(line)
    fo.close()


def TestLoadFilebd5dab72d5():
    lines = []
    loadFile("test.txt")
    t.Log("lines: ", lines)
    t.AssertEqual(lines[0], "This is line 1")
    t.AssertEqual(lines[1], "This is line 2")
    t.AssertEqual(lines[2], "This is line 3")


def TestLoadFileWithInvalidFileNamebd5dab72d5():
    lines = []
    loadFile("invalid.txt")
    t.AssertEqual(lines, [])


if __name__ == "__main__":
    t = unittest.TestLoader().loadTestsFromTestCase(TestLoadFilebd5dab72d5)
    unittest.TextTestRunner(verbosity=2).run(t)