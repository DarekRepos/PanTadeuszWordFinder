"""
Test module for the `count_multiple_words_in_file` function
from the `ptwordfinder.commands.pt_word_finder` module.

This module contains the following test cases:
1. `test_file` fixture: Creates a temporary file with mock content for testing.
2. `test_count_multiple_words_in_file_given_word_set`:
    Verifies that the correct count is returned for a given word set.
3. `test_count_multiple_words_in_file_given_empty_word_set`:
    Verifies that the count is zero for an empty word set.
4. `test_count_multiple_words_in_file_given_nonexistent_word`:
    Verifies that the count is zero for a word set with non-existent words.
5. `test_count_multiple_words_in_file_nonexistent_file`:
    Verifies that a FileNotFoundError is raised for a non-existent file.
"""

import pytest

from ptwordfinder.commands.pt_word_finder import count_multiple_words_in_file


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
    with open(test_file_path, "w", encoding="utf8") as f:
        f.write(test_content)
    return str(test_file_path)


def test_count_multiple_words_in_file_given_word_set(test_file):
    """
    When counting words in a file with a given word set,

    Args:
    test_file (str): Path of the test file.

    Verifies that:
    - The number of occurrences of words from the word set in the file is 4.
    - Sample and sample don't counts as the same words, it is case sensitive
    """
    # Given
    word_set = {"sample", "file", "count"}

    # When
    result = count_multiple_words_in_file(word_set, test_file)

    # Then
    assert result == 4


def test_count_multiple_words_in_file_given_empty_word_set(test_file):
    """
    When counting words in a file with an empty word set,

    Args:
    test_file (str): Path of the test file.

    Verifies that:
    - The count of words in the file is 0.
    """
    # Given
    word_set = set()  # empty word set

    # When
    result = count_multiple_words_in_file(word_set, test_file)

    # Then
    assert result == 0


def test_count_multiple_words_in_file_given_nonexistent_word(test_file):
    """
    When counting words in a file
    with a word set containing non-existent words,

    Args:
    test_file (str): Path of the test file.

    Verifies that:
    - The count of words in the file is 0.
    """
    # Given
    word_set = {"nonexistent", "word"}

    # When
    result = count_multiple_words_in_file(word_set, test_file)

    # Then
    assert result == 0


def test_count_multiple_words_in_file_nonexistent_file():
    """
    When counting words in a non-existent file,

    Verifies that:
    - FileNotFoundError is raised.
    """
    # Given
    word_set = {"word"}  # arbitrary word set

    # When
    with pytest.raises(FileNotFoundError):

        # Then
        count_multiple_words_in_file(word_set, "nonexistent_file.txt")
