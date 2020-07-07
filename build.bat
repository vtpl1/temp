python setup.py develop --uninstall
@RD /S /Q dist build temp.egg-info
bump2version patch --allow-dirty
pipenv-setup sync
python setup.py bdist_wheel
REM python -m PyInstaller --name temp temp/cli.py
REM python -m PyInstaller --onefile --name temp temp/cli.py
REM python -m PyInstaller --onefile --name temp --add-data "templates/__init__.py.template" temp/cli.py
python -m PyInstaller --onefile --name temp --add-data "templates/__init__.py.template" --add-data "templates/__main__.py.template" --add-data "templates/_version.py.template" --add-data "templates/.bumpversion.cfg.template" --add-data "templates/.gitignore.template" --add-data "templates/build.sh.template" --add-data "templates/cli.py.template" --add-data "templates/LICENSE.template" --add-data "templates/logging.yaml.template" --add-data "templates/Pipfile.template" --add-data "templates/README.md.template" --add-data "templates/setup.cfg.template" --add-data "templates/setup.py.template" --add-data "templates/temp.json" temp/cli.py

REM python -m PyInstaller --debug=all temp.spec
REM svn copy http://svn.example.com/repos/calc/trunk \
REM            http://svn.example.com/repos/calc/tags/release-1.0 \
REM            -m "Tagging the 1.0 release of the 'calc' project."

pip3 install -e .
