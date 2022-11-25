#!/usr/bin/env python3

from pathlib import Path

from setuptools import find_packages, setup

packages = find_packages(exclude=("tests*",))
package_data = {pkg: ["py.typed"] for pkg in packages}


setup(
    install_requires=Path("requirements.txt").read_text().splitlines(),
    packages=packages,
    package_data=package_data,
    scripts=["sortd"],
)
