#!/usr/bin/env python3

from setuptools import setup


def slurp(path: str) -> str:
    with open(path) as fd:
        return fd.read()


setup(
    name="sortd",
    version="1.0.1",
    description="sorting commands for stdin -> stdout",
    long_description=slurp("README.md"),
    long_description_content_type="text/markdown",
    author="ms-jpq",
    author_email="github@bigly.dog",
    url="https://github.com/ms-jpq/sortd",
    install_requires=["pyyaml", "toml"],
    scripts=["slines", "sjson", "syaml", "stoml"],
)
