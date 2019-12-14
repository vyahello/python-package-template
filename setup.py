from typing import IO
from setuptools import setup, find_packages


def _description() -> str:
    with open("README.md", "r") as readme:  # type: IO
        return readme.read()


setup(
    name="package-tutorial-vyahello",
    version="0.0.1",
    author="Volodymyr Yahello",
    author_email="vyahello@gmail.com",
    description="A simple example package tutorial",
    long_description=_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/vyahello/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
