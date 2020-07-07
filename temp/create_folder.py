import logging
import os
import shutil
import subprocess
import sys

LOGGER = logging.getLogger(__name__)


def create_folder(output_dir_path, pname):

    output_src_dir_path = os.path.join(output_dir_path, pname)
    if os.path.isdir(output_dir_path):
        LOGGER.warn('{} already exists!'.format(output_dir_path))
    else:
        os.makedirs(output_src_dir_path)
        LOGGER.info('{} created succesfully!'.format(output_dir_path))

    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        templates_path = os.path.join(bundle_dir, 'templates')
    else:
        templates_path = os.path.join(os.path.dirname(__file__), '..{}templates'.format(os.sep))

    LOGGER.info("File path {}".format(templates_path))

    return templates_path
