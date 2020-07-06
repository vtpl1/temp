"""Main file for temp."""
import argparse
import logging
import logging.config
import os
import shutil
import subprocess
import sys

import yaml

import temp


def setup_logging(default_path='logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """
        Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


LOGGER = logging.getLogger(__name__)


def main1():
    frozen = 'not'
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
        print('hhhhhhhhhh')
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    print('we are', frozen, 'frozen')
    print(os.listdir(bundle_dir + '/templates'))
    print('bundle dir is', bundle_dir)
    print('sys.argv[0] is', sys.argv[0])
    print('sys.executable is', sys.executable)
    print('os.getcwd is', os.getcwd())


def main():
    """CLI parsing"""
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group('Argument')
    group.add_argument('project_name', help='Project name to create')

    group = parser.add_argument_group('Options')
    group.add_argument('-v', '--version', action='version', version=temp.__version__, help='Output version number')
    group.add_argument('-o', '--output_dir', help='Output directory path', default='.')

    LOGGER.info('Running Version :: {}'.format(temp.__version__))

    # pipenv install --dev yapf bump2version mypy pylama pylint
    args = parser.parse_args()
    pname = args.project_name
    setup_logging()

    output_dir_path = os.path.join(args.output_dir, pname)

    # create project with project name
    temp.create_project(output_dir_path, pname)

    LOGGER.info('Successfully created project :: {}'.format(pname))


if __name__ == "__main__":
    main()
