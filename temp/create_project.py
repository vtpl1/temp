import logging

import temp

LOGGER = logging.getLogger(__name__)


def create_project(path, pname):
    templates_path = temp.create_folder(path, pname)
    temp.copy_templates(path, pname, templates_path)
