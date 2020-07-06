python setup.py develop --uninstall
@RD /S /Q dist build temp.egg-info
bump2version patch --allow-dirty
pipenv-setup sync
python setup.py sdist bdist_wheel
REM python -m PyInstaller --name temp temp/cli.py
REM python -m PyInstaller --onefile --name temp temp/cli.py
python -m PyInstaller --onefile --name temp --add-data 'templates/*:templates' --add-data 'templates/.bumpversion.cfg.template:templates' --add-data 'templates/.gitignore.template:templates' temp/cli.py
REM python -m PyInstaller --debug=all temp.spec
REM svn copy http://svn.example.com/repos/calc/trunk \
REM            http://svn.example.com/repos/calc/tags/release-1.0 \
REM            -m "Tagging the 1.0 release of the 'calc' project."

pip3 install -e .
