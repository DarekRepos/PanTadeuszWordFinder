# PTWordFinder

[![Build](https://github.com/DarekRepos/PanTadeuszWordFinder/actions/workflows/python-package.yml/badge.svg)](https://github.com/DarekRepos/PanTadeuszWordFinder/actions/workflows/python-package.yml)
[![Tests Status](https://github.com/DarekRepos/PanTadeuszWordFinder/blob/master/reports/coverage/coverage-unit-badge.svg)](https://github.com/DarekRepos/PanTadeuszWordFinder/blob/master/reports/coverage.xml)
[![Coverage Status](https://github.com/DarekRepos/PanTadeuszWordFinder/blob/master/reports/coverage/coverage-badge.svg)](https://github.com/DarekRepos/PanTadeuszWordFinder/tree/master/tests/unit)
[![Flake8 Status](https://github.com/DarekRepos/PanTadeuszWordFinder/blob/master/reports/flake8/flake8-badge.svg)](https://github.com/DarekRepos/PanTadeuszWordFinder/)
[![PyPi Badge](https://img.shields.io/pypi/v/PTWordFinder)](https://github.com/DarekRepos/PanTadeuszWordFinder/)
[![PyPI version](https://badge.fury.io/py/PTWordFinder.svg)](https://badge.fury.io/py/PTWordFinder)
[![Python versions](https://img.shields.io/pypi/pyversions/PTWordFinder)](https://pypi.org/project/PTWordFinder/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/DarekRepos/PanTadeuszWordFinder/actions/workflows/python-publish.yml/badge.svg)](https://github.com/DarekRepos/PanTadeuszWordFinder/actions)

Python word & pattern counter – single words, word lists or regex – originally built for Pan Tadeusz analysis

> "What specific words would you like to read?" Counting words in "Pan Tadeusz" poem

It is a Python-based command-line tool designed to efficiently find and count occurrences of specific words within text files. It offers flexible input options, supporting both individual words, patterns and word lists in various formats.

## Python version

Tested with Python >= 3.10.6

## Why

It was started as a project to exercise python language. The code helped to find specific words in a selected file. It became a command line tool that helps find any word within any file. The files can be selected by command line.

## Install

You can run the following command in your terminal to install the program from pip:

```
pip install PTWordFinder
```

This will download and install the program, along with any required dependencies.

If you prefer, you can also install the program from source:

Clone the repository containing the program code:

```
git clone https://github.com/DarekRepos/PanTadeuszWordFinder.git
```

Navigate to the cloned directory:

```
cd PanTadeuszWordFinder
```

This method requires poetry or Python build tools. If you don't have them, install poetry using `pip install poetry` or install your system's package manager's equivalent for build.

Install the program using [poetry](https://python-poetry.org/):

```
poetry install
```

The second method involves directly building the wheel and installing it, which is less commonly used.

Install the program directly:

```
python -m build
```

```
python -m pip install dist/PTWordFinder-*.whl
```

> **Note:**
> - If you install from source, you will need to have Python development tools installed. You can usually install these using your system's package manager.
> - Installing from pip is the easiest and most recommended method for most users.

## Usage

```
python word_counter.py [OPTIONS]

Options:
  -w, --words-input-file FILE     File containing words to search for (mutually exclusive with --single-word)
  -s, --searched-file FILE        Path to the text file to search in (required)
  -w, --single-word WORD          Specific word to count (mutually exclusive with --words-input-file)
  -p, --pattern PATTERN           Regular expression pattern to match
  -h, --help                      Show this help message and exit
```

**Usage Demo:**
<p align="center">
  <img src="recordings/demo.gif" alt="PTWordFinder Demo" width="600">
</p>


## Examples

Count the word "python" in `my_text.txt`:

```
python word_counter.py --single-word python --searched-file my_text.txt
```

Find the frequency of all words in `word_list.txt` in `large_file.txt`:

```
python word_counter.py --words-input-file word_list.txt --searched-file large_file.txt
```

Match instances of the regular expression `[a-z0-9]{5}` in `passwords.txt`:

```
python word_counter.py --pattern "[a-z0-9]{5}" --searched-file passwords.txt
```

## Development

If you want to contribute to the project and need to update demo recordings (GIFs), you can find the full technical instructions here: [Recording Guide](record.md).

If you want to contribute to the project and need to update demo recordings (GIFs), you can find the full technical instructions here: [Recording Guide](record.md).
