"""Main file for temp."""
import argparse
from temp._version import __version__

def main():
    """CLI parsing"""
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group('Argument')
    group.add_argument('project_name', help='Project name to create')

    group = parser.add_argument_group('Options')
    group.add_argument('-v', '--version', action='version', version=__version__, help='Output version number')

    print("Hello world %s" % __version__)
    # pipenv install --dev yapf bump2version mypy pylama pylint
    args = parser.parse_args()
    pname = args.project_name
    print(pname)


if __name__ == "__main__":
    main()
