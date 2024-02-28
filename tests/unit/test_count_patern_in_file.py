import io
import os
from unittest.mock import mock_open, patch
import pytest
from ptwordfinder.commands.PTWordFinder import count_pattern_in_file


@pytest.fixture
def mock_file():
    # Create a StringIO object to simulate a file
    file_content = "This is a test file without any test matches.\n"
    return io.StringIO(file_content)


def test_count_pattern_in_file_no_matches(mock_file):
    """
    Test count_pattern_in_file function with no matches in the file.

    Args:
        mock_file: Fixture providing a mocked file object.

    Verifies that:
    - The count of the specified pattern in the file is 0.
    """
    # Given
    pattern = r"899"
    # When
    with patch("builtins.open", return_value=mock_file):
        result = count_pattern_in_file(pattern, "test_file.txt")
    # Then
    assert result == 0


def test_count_pattern_in_file_matches(mock_file):
    """
    Test count_pattern_in_file function with matches in the file.

    Args:
        mock_file: Fixture providing a mocked file object.

    Verifies that:
    - The count of the specified pattern in the file is accurate.
    """
    # Given
    pattern = "test"
    # When
    with patch("builtins.open", return_value=mock_file):
        result = count_pattern_in_file(pattern, "test_file.txt")
        print(result)
    # Then
    assert result == 2


def test_count_pattern_in_file_empty_file():
    """
    Test count_pattern_in_file function with an empty file.

    Verifies that:
    - The count of the specified pattern in an empty file is 0.
    """
    # Given
    pattern = r"\w+"
    # When
    with patch("builtins.open", mock_open(read_data="")) as mock_file:
        result = count_pattern_in_file(pattern, "test_file.txt")
    # Then
    assert result == 0


def test_count_pattern_in_file_blank_lines():
    """
    Test count_pattern_in_file function with blank lines in the file.

    Verifies that:
    - The count of the specified pattern in a file with only blank lines is 0.
    """
    # Given
    pattern = r"\n"
    # When
    with patch("builtins.open", mock_open(read_data="\n\n\n")) as mock_file:
        result = count_pattern_in_file(pattern, "test_file.txt")
    # Then
    assert result == 0


def test_empty_file():
    """
    Test count_pattern_in_file function with an empty file.

    Verifies that:
    - The count of any pattern in an empty file is 0.
    """
    pattern = "word"
    with open("empty_file.txt", "w"):
        pass

    assert count_pattern_in_file(pattern, "empty_file.txt") == 0

    # Clean up test files
    os.remove("empty_file.txt")


def test_single_match():
    """
    Test count_pattern_in_file function with a single match in the file.

    Verifies that:
    - The count of the specified pattern in a file with one match is 1.
    """
    pattern = "word"
    with open("single_match.txt", "w") as file:
        file.write("This is a test line with word.\n")

    assert count_pattern_in_file(pattern, "single_match.txt") == 1

    # Clean up test files
    os.remove("single_match.txt")


def test_multiple_matches():
    """
    Test count_pattern_in_file function with multiple matches in the file.

    Verifies that:
    - The count of the specified pattern in a file with multiple matches
      is equal to the number of occurrences.
    """
    pattern = "the"
    with open("multiple_matches.txt", "w") as file:
        file.write("This is the first line. The second line also has the.\n")
        file.write("A third line, but without the pattern.\n")

    assert count_pattern_in_file(pattern, "multiple_matches.txt") == 3

    # Clean up test files
    os.remove("multiple_matches.txt")


def test_case_insensitive():
    """
    Test count_pattern_in_file function with case-insensitive matching.

    Verifies that:
    - The count of the specified pattern in a file is case-insensitive.
    """
    pattern = "Word"  # Case-insensitive
    with open("single_match.txt", "w") as file:
        file.write("This is a test line with word.\n")

    assert count_pattern_in_file(pattern, "single_match.txt") == 0

    # Clean up test files
    os.remove("single_match.txt")


def test_nonblank_lines():
    """
    Test count_pattern_in_file function with non-blank lines only.

    Verifies that:
    - The count of the specified pattern considers only non-blank lines
      in the file.
    """
    pattern = "line"
    with open("mixed_lines.txt", "w", encoding="utf8") as file:
        file.write("This is a line with word.\n")
        file.write("\n")  # Blank line
        file.write("Another line\n")

    assert count_pattern_in_file(pattern, "mixed_lines.txt") == 2

    # Clean up test files
    os.remove("mixed_lines.txt")


def test_multiple_spaces():
    """
    Test count_pattern_in_file function with multiple spaces surrounding the pattern.

    Verifies that:
    - The count of the specified pattern considers the pattern regardless of surrounding spaces.
    """
    pattern = "word"
    with open("multiple_spaces.txt", "w") as file:
        file.write("This   is  a line with  word. \n")

    assert count_pattern_in_file(pattern, "multiple_spaces.txt") == 1

    # Clean up test files
    os.remove("multiple_spaces.txt")


def test_invalid_file():
    """
    Test count_pattern_in_file function with a non-existent file.

    Verifies that:
    - The function raises a FileNotFoundError when the specified file does not exist.
    """
    pattern = "word"
    with pytest.raises(FileNotFoundError):
        count_pattern_in_file(pattern, "nonexistent_file.txt")
