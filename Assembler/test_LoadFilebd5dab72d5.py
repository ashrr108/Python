
        lines.append(line)
    fo.close()


 
         import sys
from __future__ import print_function

def loadFile(fileName):
    """
    loadFile: This function loads the file and reads its lines.
    """
    global lines
    fo = open(fileName)
    for line in fo:
        lines.append(line)
    fo.close()


class TestLoadFile5dab77d2(unittest.TestCase):

    def setUp(self):
        self.lines = []

    def testLoadFileSuccess(self):
        loadFile('test.txt')
        self.assertEqual(self.lines, ['line1', 'line2'])

    def testLoadFileFailure(self):
        loadFile('invalid.txt')
        self.assertEqual(self.lines, [])

if __name__ == '__main__':
    unittest.main()