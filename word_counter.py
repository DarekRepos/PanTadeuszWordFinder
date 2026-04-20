"""
This module provides tools for counting the occurrences of words
or patterns in a text file.
"""

from typing import Iterator, List, Set

import re
import sys
import time

import click


@click.command()
@click.option(
    "--words-input-file",
    "-i",
    type=click.File("r", lazy=True),
    help="File containing words to search for",
)
@click.option(
    "--searched-file",
    "-s",
    type=click.Path(exists=True),
    required=True,
    help="Text file to search in",
)
@click.option(
    "--single-word",
    "-w",
    type=click.STRING,
    help="Specific word to count (exclusive to --words-input-file)",
)
@click.option("--pattern", "-p", help="Regular expression pattern to match")
def calculate_words(
    words_input_file: click.File,
    searched_file: str,
    single_word: str,
    pattern: str,
) -> None:
    op1 = "--words-input-file"
    op2 = "--single-word"
    op3 = "--pattern"

    if words_input_file and single_word:
        click.echo(f"Error: {op1} and {op2} are mutually exclusive.", err=True)
        sys.exit(1)

    if not (words_input_file or single_word or pattern):
        click.echo(
            f"Error: At least one of {op1}, {op2}, or {op3} must be provided.",
            err=True,
        )
        sys.exit(1)

    start_time = time.time()

    if words_input_file:
        with open(words_input_file.name, "r", encoding="utf8") as file:
            word_list = [elt.strip() for elt in file.readlines()]
            words = set(word_list)
            counter = count_multiple_words_in_file(words, searched_file)
            file1 = words_input_file.name
            file2 = searched_file
        print(f"Found {counter} matching words from '{file1}' in '{file2}'.")

    elif single_word:
        counter = count_word_in_file(single_word, searched_file)
        print(f"Found '{single_word}' {counter} times in '{searched_file}'.")

    else:
        c = count_pattern_in_file(pattern, searched_file)
        with open(searched_file, "r", encoding="utf8") as f:
            print(f"Found {c} matches for pattern '{pattern}' in '{f.name}'.")

    stop_time = time.time()
    elapsed_time = stop_time - start_time
    print(f"Time elapsed: {elapsed_time:.1f} seconds")


def count_multiple_words_in_file(words: Set[str], searched_file: str) -> int:
    counter = 0
    with open(searched_file, "r", encoding="utf8") as file:
        for line in non_blank_lines(file):
            for word in line:
                if word in words:
                    counter += 1
    return counter


def count_word_in_file(word: str, searched_file: str) -> int:
    try:
        count = 0
        with open(searched_file, "r", encoding="utf8") as file:
            for line in file:
                count += line.count(word)
        return count
    except FileNotFoundError:
        click.echo(f"Error: Path '{searched_file}' does not exist.", err=True)
        raise


def count_pattern_in_file(pattern: str, searched_file: str) -> int:
    sanitized_pattern = sanitize_pattern(pattern)
    counter = 0
    with open(searched_file, "r", encoding="utf8") as file:
        for line in file:
            counter += sum(1 for _ in re.finditer(sanitized_pattern, line))
    return counter


def non_blank_lines(text_file: Iterator[str]) -> Iterator[List[str]]:
    for line in text_file:
        line = line.strip()
        if line:
            text = re.split(r"\s+", line)
            stripped_line = []
            for item in text:
                stripped = "".join(ch for ch in item if ch.isalnum())
                stripped_line.append(stripped)
            yield stripped_line


def sanitize_pattern(pattern: str) -> str:
    if not isinstance(pattern, str):
        raise TypeError("Input must be a string")
    return re.escape(pattern)


if __name__ == "__main__":
    calculate_words()  # pylint: disable=no-value-for-parameter
