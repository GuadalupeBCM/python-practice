#!/usr/bin/env python
from pathlib import Path
from setuptools import setup, find_packages

root = Path(__file__).parent
with open(root / "requirements.txt") as f:
    install_requires = f.readlines()

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="python-practice",
    version="0.0.1",
    description="code for Python practice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Guadalupe Perez",
    author_email="guadalupejovitayasmin.perezvega@bcm.edu",
    url="https://github.com/YasminBCM/python-practice",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=install_requires,
)
