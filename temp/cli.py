"""Main file for temp."""
import argparse
import logging
import logging.config
import os
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
    LOGGER.info('Next steps 1) :: cd {}'.format(pname))
    LOGGER.info('           2) :: pipenv install --dev')
    LOGGER.info('           3) :: pipenv shell')
    LOGGER.info('           4) :: nano /etc/hosts')
    LOGGER.info('                 add "192.168.1.186    pypi.videonetics.com"')
    LOGGER.info('           5) :: nano ~/.pypirc')
    LOGGER.info('                 write ::\n\n[distutils]\nindex-servers =\n  vtpl\n\n[vtpl]\nrepository: http://pypi.videonetics.com:8080\nusername:vtpl\npassword:Vtpl@123\n\n')
    LOGGER.info('           6) :: . build.sh')
    LOGGER.info('The exexutable will be available at {0}/dist with the name {0}'.format(pname))



if __name__ == "__main__":
    main()
