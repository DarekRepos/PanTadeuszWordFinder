from unittest import mock

from ptwordfinder.commands.PTWordFinder import nonblank_lines


def test_empty_file():
    with open("empty_file.txt", "w"):
        pass

    lines = list(nonblank_lines(open("empty_file.txt")))
    assert lines == []


def test_single_nonblank_line():
    with open("single_line.txt", "w") as file:
        file.write("This is a line.\n")

    lines = list(nonblank_lines(open("single_line.txt")))
    assert lines == [["This", "is", "a", "line"]]


def test_multiple_nonblank_lines():
    with open("multiple_lines.txt", "w") as file:
        file.write("Line 1.\n")
        file.write("\n")  # Blank line
        file.write("Line 2\n")

    lines = list(nonblank_lines(open("multiple_lines.txt")))
    assert lines == [["Line", "1"], ["Line", "2"]]


def test_mixed_content():
    with open("mixed_content.txt", "w") as file:
        file.write("  Some text  \n")
        file.write("\n")
        file.write(" More text, with special characters!@#$%^&*()\n")

    lines = list(nonblank_lines(open("mixed_content.txt")))
    assert lines == [
        ["Some", "text"],
        ["More", "text", "with", "special", "characters"],
    ]


def test_non_alphanumeric():
    with open("non_alphanumeric.txt", "w") as file:
        file.write("123abc!@#$\n")
        file.write("漢字日本語\n")

    lines = list(nonblank_lines(open("non_alphanumeric.txt")))
    assert lines == [["123abc"], ["漢字日本語"]]
