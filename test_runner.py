from argparse import ArgumentParser

import pytest

parser = ArgumentParser()
parser.add_argument('-b', '--browser', dest='browser',
                    help='Browser name on which the tests will be run i.e. firefox, chrome',
                    metavar="BROWSER")
_args = parser.parse_args()

if __name__ == "__main__":
    pytest.main(['--browser', _args.browser or 'chrome'])
