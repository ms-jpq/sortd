#!/usr/bin/env python3

from os import chdir
from os.path import dirname

from setuptools import setup

__dir__ = dirname(__file__)
chdir(__dir__)


def slurp(path: str) -> str:
    with open(path) as fd:
        return fd.read()


setup(
    name="sortd",
    version="1.0.11",
    description="sorting commands for stdin -> stdout",
    long_description=slurp("README.md"),
    long_description_content_type="text/markdown",
    author="ms-jpq",
    author_email="github@bigly.dog",
    url="https://github.com/ms-jpq/sortd",
    install_requires=slurp("requirements.txt").splitlines(),
    packages=["sortd"],
    scripts=["slines", "sjson", "syaml", "stoml"],
)
