python setup.py develop --uninstall
rm -rf dist build
bump2version patch
pipenv-setup sync
python setup.py bdist_wheel
#python -m PyInstaller --name temp temp/cli.py
python -m PyInstaller --onefile --name temp temp/cli.py
# svn copy http://svn.example.com/repos/calc/trunk \
#            http://svn.example.com/repos/calc/tags/release-1.0 \
#            -m "Tagging the 1.0 release of the 'calc' project."

pip3 install -e .
