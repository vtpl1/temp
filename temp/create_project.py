import logging

import temp

LOGGER = logging.getLogger(__name__)


def create_project(path, pname):
    temp.create_folder(path, pname)
