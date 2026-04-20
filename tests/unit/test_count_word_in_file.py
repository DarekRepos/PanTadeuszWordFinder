"""
Test module for the `count_word_in_file` function from the
`ptwordfinder.commands.pt_word_finder` module.

This module contains the following test cases:
1. `test_count_word_in_file`: Verifies that the function correctly counts the
   occurrences of a known word in a file.
2. `test_word_not_found`: Verifies that the function returns a count of 0 for
   a word that is not present in the file.
3. `test_file_not_found`: Verifies that the function raises a FileNotFoundError
   when attempting to count a word in a non-existent file.

The module also includes a fixture:
- `test_file`: Creates a temporary file with predefined content for testing
  purposes.
"""

import pytest
from ptwordfinder.commands.pt_word_finder import count_word_in_file

# Mocking a file content for testing
mock_file_content = """
This is a sample file.
It contains words that we will search for.
Sample file has words to count.
"""


@pytest.fixture
def test_file(tmpdir):
    """
    Given a temporary directory,
    Create a temporary file with some content for testing.

    Returns:
    str: Path of the temporary file.
    """
    test_content = mock_file_content
    test_file_path = tmpdir.join("test-file.txt")
    with open(test_file_path, "w", encoding="utf-8") as f:
        f.write(test_content)
    return str(test_file_path)


def test_count_word_in_file(test_file):
    """
    Test the function count_word_in_file with a known word in the file.

    Args:
    test_file (str): Path of the test file.

    Verifies that:
    - The count of the word "file" in the file is 2.
    - The count of the words "file." and "file" count as same word
    """
    # Given
    word = "file"
    # When
    result = count_word_in_file(word, test_file)
    # Then
    assert result == 2


def test_word_not_found(test_file):
    """
    Test the function count_word_in_file with a word not in the file.

    Args:
    test_file (str): Path of the test file.

    Verifies that:
    - The count of the word "hello" in the file is 0.
    """
    # Given
    word = "hello"
    # When
    result = count_word_in_file(word, test_file)
    # Then
    assert result == 0


def test_file_not_found():
    """
    Test the function count_word_in_file with a non-existent file.

    Verifies that:
    - FileNotFoundError is raised when trying to access a non-existent file.
    """
    # When
    with pytest.raises(FileNotFoundError):
        # Then
        count_word_in_file("test", "non_existent_file.txt")
