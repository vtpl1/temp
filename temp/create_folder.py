import logging
import os
import pkgutil
LOGGER = logging.getLogger(__name__)


def create_folder(output_dir_path, pname):

    output_src_dir_path = os.path.join(output_dir_path, pname)
    if os.path.isdir(output_dir_path):
        LOGGER.warn('{} already exists!'.format(output_dir_path))
    else:
        os.makedirs(output_src_dir_path)
        LOGGER.info('{} created succesfully!'.format(output_dir_path))

    old_project_file = 'templates/.bumpversion.cfg.template'
    template = pkgutil.get_data('templates', '.bumpversion.cfg.template').decode('UTF-8', 'ignore')
    #with open(old_project_file) as template, open('{}/.bumpversion.cfg'.format(output_dir_path), 'w') as new_project_file:
    with open('{}/.bumpversion.cfg'.format(output_dir_path), 'w') as new_project_file:
        new_project_file.write(template.replace('$pname', pname))

        # lines = template.readlines()
        # for idx, line in enumerate(lines):
        #     if '$pname' in line:
        #         new_line = line.replace('$pname', pname)
        #         lines[idx] = new_line
        # new_project_file.writelines(lines)
    LOGGER.info('.bumpversion.cfg created succesfully!')

    # old_project_file = 'templates/.gitignore.template'
    # with open(old_project_file) as template, open('{}/.gitignore'.format(output_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('.gitignore created succesfully!')

    # old_project_file = 'templates/build.sh.template'
    # with open(old_project_file) as template, open('{}/build.sh'.format(output_dir_path), 'w') as new_project_file:
    #     lines = template.readlines()
    #     for idx, line in enumerate(lines):
    #         if '$pname' in line:
    #             new_line = line.replace('$pname', pname)
    #             lines[idx] = new_line
    #     new_project_file.writelines(lines)
    # LOGGER.info('build.sh created succesfully!')

    # old_project_file = 'templates/LICENSE.template'
    # with open(old_project_file) as template, open('{}/LICENSE'.format(output_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('LICENSE created succesfully!')

    # old_project_file = 'templates/logging.yaml.template'
    # with open(old_project_file) as template, open('{}/logging.yaml'.format(output_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('logging.yaml created succesfully!')

    # old_project_file = 'templates/Pipfile.template'
    # with open(old_project_file) as template, open('{}/Pipfile'.format(output_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('Pipfile created succesfully!')

    # old_project_file = 'templates/README.md.template'
    # with open(old_project_file) as template, open('{}/REAME.md'.format(output_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('REAME.md created succesfully!')

    # old_project_file = 'templates/setup.cfg.template'
    # with open(old_project_file) as template, open('{}/setup.cfg'.format(output_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('setup.cfg created succesfully!')

    # old_project_file = 'templates/setup.py.template'
    # with open(old_project_file) as template, open('{}/setup.py'.format(output_dir_path), 'w') as new_project_file:
    #     lines = template.readlines()
    #     for idx, line in enumerate(lines):
    #         if '$pname' in line:
    #             new_line = line.replace('$pname', pname)
    #             lines[idx] = new_line
    #     new_project_file.writelines(lines)
    # LOGGER.info('setup.py created succesfully!')

    # old_project_file = 'templates/__init__.py.template'
    # with open(old_project_file) as template, open('{}/__init__.py'.format(output_src_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('__init__.py created succesfully!')

    # old_project_file = 'templates/__main__.py.template'
    # with open(old_project_file) as template, open('{}/__main__.py'.format(output_src_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('__main__.py created succesfully!')

    # old_project_file = 'templates/_version.py.template'
    # with open(old_project_file) as template, open('{}/_version.py'.format(output_src_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('_version.py created succesfully!')

    # old_project_file = 'templates/cli.py.template'
    # with open(old_project_file) as template, open('{}/cli.py'.format(output_src_dir_path), 'w') as new_project_file:
    #     new_project_file.writelines(template.readlines())
    # LOGGER.info('cli.py created succesfully!')

    # pipenv_path = shutil.which('pipenv')
    # os.chdir(output_dir_path)
    # subprocess.run([pipenv_path, 'install', '--dev', pname], check=True)
