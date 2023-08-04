This package is for investigating hyperproperty controller synthesis with examples from obfuscation against aware eavesdroppers.
This project utilizes the [MDESops](https://gitlab.eecs.umich.edu/M-DES-tools/desops) library.

## Installation

In the main directory, the project can be installed with:

    poetry install

If you would rather use a local version of M-DESops instead of the most recent version, in `pyproject.toml` comment the line:

    DESops = {git="https://gitlab.eecs.umich.edu/M-DES-tools/desops.git"}

and uncomment the line:

    # DESops = {path="../desops"}

The project also relies on [Quabs](https://github.com/ltentrup/quabs).
After installing using instructions there, you can either
1. Ensure the installation directory (build) is on the path
2. Create an environment variable `HYPER_ENF_QUABS_DIR` set to the installation directory
3. Create a file named `.env` in the Python project root directory with the line

    HYPER_ENF_QUABS_DIR = path/to/quabs/

On Windows if Quabs did not install, it can be installed on WSL and used from there.
To do this, create an environment variable `HYPER_ENF_WSL` set to `1`,
and set the environment variable `HYPER_ENF_QUABS_DIR` to the ``scripts/wsl`` directory in this project
(it needs to be an absolute path).

The project also uses Pyeda which is installed from the ``pyproject.toml`` file.
You will need to uncomment the appropriate line in this file depending on your operating system.

## Pre-commit hooks
To ensure code uniformity, you can setup pre-commit hooks in the ``python`` directory by running

    poetry run pre-commmit install

Then whenever you make a commit, the checks are run possibly changing the code.
If any changes are made, you will need to add the changes before trying to commit again.

## Tests
This repository employs [pytest](https://docs.pytest.org/en/latest/) to write tests.
All tests are located in `tests` directory, and must be written with the formats of
`pytest`.

You can execute tests by the following command:
```
poetry run pytest
```
