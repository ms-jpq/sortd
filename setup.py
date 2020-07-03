#!/usr/bin/env python3

from setuptools import setup


def slurp(path: str) -> str:
    with open(path) as fd:
        return fd.read()


setup(
    name="sorted",
    version="1.0.0",
    description="",
    long_description=slurp("README.md"),
    long_description_content_type="text/markdown",
    author="ms-jpq",
    author_email="github@bigly.dog",
    url="",
    scripts=["sjson", "syaml", "stoml"],
)
