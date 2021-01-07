#!/usr/bin/env python3

from pathlib import Path

from setuptools import find_packages, setup

packages = find_packages(exclude=("tests*",))
package_data = {pkg: ("py.typed",) for pkg in packages}


setup(
    name="sortd",
    version="1.1.4",
    install_requires=Path("requirements.txt").read_text().splitlines(),
    description="sorting commands for stdin -> stdout",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="ms-jpq",
    author_email="github@bigly.dog",
    url="https://github.com/ms-jpq/sortd",
    packages=packages,
    package_data=package_data,
    scripts=("sortd",),
)
