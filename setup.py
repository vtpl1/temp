"""Setup file for temp python module"""
from setuptools import find_packages, setup
from os import path

exec(open("temp/_version.py").read())

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="temp",
    version=__version__,
    author="Monotosh Das",
    author_email="monotosh.das@videonetics.com",
    description="🚀 A CLI tool for scaffolding any Python Projects 🚀",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="scaffold python project cli",
    license="MIT",
    url="https://github.com/vtpl1/temp",
    packages=find_packages(),
    entry_points={"console_scripts": ["temp=temp.cli:main"],},
    install_requires=[],
    extras_require={
        "test": ["pytest", "flake8"],
        "develop": [
            "yapf",
            "bump2version",
            "mypy",
            "pylama",
            "pylint",
            "pycodestyle",
            "pipenv-setup",
        ],
    },
    tests_require=["pytest", "flake8"],
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
)
