import logging
import os
import shutil
import subprocess
import sys

LOGGER = logging.getLogger(__name__)


def copy_templates(output_dir_path, pname, templates_path):

    template_files = []
    template_ext = '.template'
    template_ext_size = - len(template_ext)
    for root, _, filenames in os.walk(templates_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if file_path.endswith(template_ext):
                template_files.append(file_path)

    new_project_file_list = list()
    for template in template_files:
        template_list = template.split(os.sep)
        new_project_file = os.path.join(output_dir_path, os.sep.join(template_list[template_list.index('templates') + 1:]))[:template_ext_size]
        if 'pname' in new_project_file:
            new_project_file = new_project_file.replace('pname', pname)

        new_project_file_list.append(new_project_file)

    for old_project_file, new_project_file_path in zip(template_files, new_project_file_list):
        with open(old_project_file, 'r') as template, open(new_project_file_path, 'w') as new_project_file:
            lines = template.readlines()
            for idx, line in enumerate(lines):
                if '$pname' in line:
                    new_line = line.replace('$pname', pname)
                    lines[idx] = new_line
            new_project_file.writelines(lines)
            LOGGER.info('{} created succesfully!'.format(new_project_file_path))

    LOGGER.info('Install pipenv and run!')
    # pipenv_path = shutil.which('pipenv')
    # if pipenv_path is None:
    #     LOGGER.warn('Pipenv not found! trying to install using pip3')
    #     pip_path = shutil.which('pip3')
    #     if pip_path is None:
    #         LOGGER.error('pip3 not found! Are you sure you are developing python project?')
    #     else:
    #         subprocess.run([pip_path, 'install', 'pipenv'], check=True)
            

    # pipenv_path = shutil.which('pipenv')
    # if pipenv_path is None:
    #     LOGGER.error('Pipenv still not found!')
    # else:
    #     LOGGER.warn('Pipenv found!')
    #     os.chdir(output_dir_path)
    #     subprocess.run([pipenv_path, 'install', '--dev', pname], check=True)
    #     LOGGER.info('Pipenv created succesfully!')
