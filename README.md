# ohdevtool - OpenHouse Dev Tool

Welcome to the ohdevtool project! This repository contains a collection of development tools for the OpenHouse project.

## Installation

This tool is meant to be published in a private repository and installed via: `pip install -i https://<repository-url> ohdevtool`

You are welcome to build and modify it yourself and install it locally.  You will first need the `build` package, typically installed by `pip install build`.
Then compile this into a package by running `python -m build` from the root of the directory.  Finally install the package and its dependencies with `pip -install .`

If you are interested in learning and trying an editable install, you can [read about it here](https://setuptools.pypa.io/en/latest/userguide/development_mode.html)

Any installation will add both the main package in `site-packages` as well as the console scripts `ohdevtool` and `odt`.

## Usage examples

Taking advantage of the console scripts, you can: 

- Use esphome to generate the source files, modify it for PlatformIO and kick off the PIO build for the project in the YAML:
    `ohdevtool build <YAML file>`

- Run the unit tests for the project in the YAML:
    `odt test <YAML file>`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
