import os
from unittest import mock

from ptwordfinder.commands.PTWordFinder import non_blank_lines


def test_empty_file():
    """
    Test non_blank_lines function with an empty file.

    Verifies that:
    - The function returns an empty list for an empty file.
    """
    with open("empty_file.txt", "w"):
        pass

    lines = list(non_blank_lines(open("empty_file.txt")))
    assert lines == []

    # Clean up test files
    os.remove("empty_file.txt")


def test_single_non_blank_line():
    """
    Test non_blank_lines function with a single non-blank line.

    Verifies that:
    - The function returns a list containing all words from the single non-blank line.
    """
    with open("single_line.txt", "w") as file:
        file.write("This is a line.\n")

    lines = list(non_blank_lines(open("single_line.txt")))
    assert lines == [["This", "is", "a", "line"]]

    # Clean up test files
    os.remove("single_line.txt")


def test_multiple_non_blank_lines():
    """
    Test non_blank_lines function with multiple non-blank lines.

    Verifies that:
    - The function returns a list containing all words from each non-blank line.
    - Blank lines are ignored.
    """
    with open("multiple_lines.txt", "w") as file:
        file.write("Line 1.\n")
        file.write("\n")  # Blank line
        file.write("Line 2\n")

    lines = list(non_blank_lines(open("multiple_lines.txt")))
    assert lines == [["Line", "1"], ["Line", "2"]]

    # Clean up test files
    os.remove("multiple_lines.txt")


def test_mixed_content():
    """
    Test non_blank_lines function with mixed content and whitespace.

    Verifies that:
    - The function returns a list containing all words from non-blank lines, removing leading and trailing whitespaces.
    """
    with open("mixed_content.txt", "w") as file:
        file.write("  Some text  \n")
        file.write("\n")
        file.write(" More text, with special characters!@#$%^&*()\n")

    lines = list(non_blank_lines(open("mixed_content.txt")))
    assert lines == [
        ["Some", "text"],
        ["More", "text", "with", "special", "characters"],
    ]

    # Clean up test files
    os.remove("mixed_content.txt")


def test_non_alphanumeric():
    """
    Test non_blank_lines function with non-alphanumeric characters.

    Verifies that:
    - The function returns a list containing all words from non-blank lines, including non-alphanumeric characters.
    """
    with open("non_alphanumeric.txt", "w") as file:
        file.write("123abc!@#$\n")
        file.write("漢字日本語\n")

    lines = list(non_blank_lines(open("non_alphanumeric.txt")))
    assert lines == [["123abc"], ["漢字日本語"]]

    # Clean up test files
    os.remove("non_alphanumeric.txt")
