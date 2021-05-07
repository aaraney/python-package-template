
## File purposes
- `pyproject.toml`: Configure what tools are needed to actually build the package
- `setup.cfg`: configure python package. Defile name, author, email, dependencies, etc.
  (This use to all be defined in `setup.py`, not preferred anymore)
- `setup.py`: Legacy way of defining package configuration
- `.gitignore`: Directories, files, and file types that you want git to ignore (these
  will not show up as `untracked` when you run `git status`)
- `mypackage`: In this template, the python package itself
- `mypackage/__init__.py`: file that tells python, this is a package (or sub-package).
  If you wanted another folder to put code in inside of `mypackage`, it would need to
include a `__init__.py` to be discovered and included in `mypackage`. 


## Helpful links
[setup.cfg](https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html)
