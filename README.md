## File purposes

- `pyproject.toml`: Configure what tools are needed to actually build the package
- `setup.cfg`: configure python package. Defile name, author, email, dependencies, etc.
  (This use to all be defined in `setup.py`, not preferred anymore)
- `.gitignore`: Directories, files, and file types that you want git to ignore (these
  will not show up as `untracked` when you run `git status`)
- `mypackage`: In this template, the python package itself
- `mypackage/__init__.py`: file that tells python, this is a package (or sub-package).
  If you wanted another folder to put code in inside of `mypackage`, it would need to
  include a `__init__.py` to be discovered and included in `mypackage`.
- `LICENSE`: An open source license, in this case MIT License, that protects
  contributors and users. Look to [choosealicense.com](https://choosealicense.com/) for
  more information and other license options.

## Setup virtual environment

Create virtual env to install this package into. This creates an isolated place to
install your package and others.

`python -m venv venv `

Activate virtual env

`. ./venv/bin/activate`

If you ever need to deactivate just run:

`deactivate`

## How to install

This will install the code in an editiable form (`-e`). So, as you update your code you
will not need to re-install.

`pip install -e .`

## Helpful links

[setup.cfg](https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html)
