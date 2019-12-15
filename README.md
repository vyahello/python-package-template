[![Release](https://img.shields.io/badge/release-0.0.1-red)](https://test.pypi.org/project/package-tutorial-vyahello/#description)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

[![Hits-of-Code](https://hitsofcode.com/github/vyahello/python-package-template)](https://hitsofcode.com/view/github/vyahello/python-package-template)

# Python package template

This project is aimed to provide instructions to build own python package from the scratch.
All steps are used from [packaging-projects](https://packaging.python.org/tutorials/packaging-projects) official tutorial.

## Tools
- python 3.8
- [black](https://black.readthedocs.io/en/stable/)
- [pylint](https://www.pylint.org/)

## Usage

There are couple of steps you have to accomplish to have own python package:
- Make sure you have package ready to be shipped e.g [example](example)
- Create bunch of meta files: [README.md](README.md), [LICENSE.md](LICENSE.md) and [requirements.txt](requirements.txt) files
- Create [setup.py](setup.py) file
- Generate distribution packages
  - Update `setuptools` and `wheel`:
    ```bash
    ➜ pip install --user --upgrade setuptools wheel
    ```
  - Run command from the same directory where `setup.py` is located:
    ```bash
    ➜ pip setup.py sdist bdist_wheel
    ```
  - You should see newly created `dist/` directory with `.tar.gz` extension file
- Upload package to PIP (python package index)
  - Create test account on [https://test.pypi.org/account/register](https://test.pypi.org/account/register)
  - Install `twine` package
    ```bash
    ➜ pip install --user --upgrade twine
    ```
  - Upload all of the archives under `dist/`
    ```bash
    ➜ python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    ```
- Install brand new python package
  ```bash
  pip install --index-url https://test.pypi.org/simple/ --no-deps package-tutorial-vyahello
  ```
  > from example import tutorial
  >
  > t = tutorial.Tutorial("foo", "bar")
  >
  > t.meta()

## Meta

Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

## Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies