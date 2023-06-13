from __future__ import print_function
import sys
import unittest
from unittest.mock import patch, MagicMock


def main():
    """
    reads textfiles from the command-line and interprets them.
    """

    # [1:] because the first argument is the program itself.
    for arg in sys.argv[1:]:

        resetInterpreter()  # resets interpreter mind

        try:

            loadFile(arg)
            scan()
            registerLabels()
            parser()

        except Exception as e:

            print(f"Error: {e}")


def resetInterpreter():
    pass


def loadFile(arg):
    pass


def scan():
    pass


def registerLabels():
    pass


def parser():
    pass


class TestMain(unittest.TestCase):

    def test_main_success(self):
        with patch('sys.argv', ['main.py', 'file1.txt']):
            mock_resetInterpreter = MagicMock()
            mock_loadFile = MagicMock()
            mock_scan = MagicMock()
            mock_registerLabels = MagicMock()
            mock_parser = MagicMock()

            with patch('builtins.resetInterpreter', mock_resetInterpreter), \
                 patch('builtins.loadFile', mock_loadFile), \
                 patch('builtins.scan', mock_scan), \
                 patch('builtins.registerLabels', mock_registerLabels), \
                 patch('builtins.parser', mock_parser):

                main()

            mock_resetInterpreter.assert_called_once()
            mock_loadFile.assert_called_once_with('file1.txt')
            mock_scan.assert_called_once()
            mock_registerLabels.assert_called_once()
            mock_parser.assert_called_once()

    def test_main_exception(self):
        with patch('sys.argv', ['main.py', 'file1.txt']):
            mock_resetInterpreter = MagicMock()
            mock_loadFile = MagicMock(side_effect=Exception('File not found'))
            mock_scan = MagicMock()
            mock_registerLabels = MagicMock()
            mock_parser = MagicMock()

            with patch('builtins.resetInterpreter', mock_resetInterpreter), \
                 patch('builtins.loadFile', mock_loadFile), \
                 patch('builtins.scan', mock_scan), \
                 patch('builtins.registerLabels', mock_registerLabels), \
                 patch('builtins.parser', mock_parser), \
                 patch('builtins.print') as mock_print:

                main()

            mock_resetInterpreter.assert_called_once()
            mock_loadFile.assert_called_once_with('file1.txt')
            mock_scan.assert_not_called()
            mock_registerLabels.assert_not_called()
            mock_parser.assert_not_called()
            mock_print.assert_called_once_with('Error: File not found')


if __name__ == "__main__":
    unittest.main()