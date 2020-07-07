python setup.py develop --uninstall
rm -rf dist build *.egg-info
bump2version patch --allow-dirty
pipenv-setup sync
# python setup.py bdist_wheel
python setup.py bdist_wheel upload -r vtpl
#python -m PyInstaller --name temp temp/cli.py
python -m PyInstaller --onefile --name temp \
--add-data 'templates/build.sh.template:templates' \
--add-data 'templates/LICENSE.template:templates' \
--add-data 'templates/logging.yaml.template:templates' \
--add-data 'templates/Pipfile.template:templates' \
--add-data 'templates/README.md.template:templates' \
--add-data 'templates/setup.cfg.template:templates' \
--add-data 'templates/setup.py.template:templates' \
--add-data 'templates/.bumpversion.cfg.template:templates' \
--add-data 'templates/.gitignore.template:templates' \
--add-data 'templates/.svnignore.template:templates' \
--add-data 'templates/pname/*:templates/pname' \
temp/cli.py
#python -m PyInstaller --debug=all temp.spec
# svn copy http://svn.example.com/repos/calc/trunk \
#            http://svn.example.com/repos/calc/tags/release-1.0 \
#            -m "Tagging the 1.0 release of the 'calc' project."

pip3 install -e .
# pip3 install --trusted-host pypi.videonetics.com -i http://pypi.videonetics.com:8080/simple/ temp
# pip3 install --trusted-host pypi.videonetics.com -U -i http://pypi.videonetics.com:8080/simple/ temp
