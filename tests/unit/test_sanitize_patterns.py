import pytest

from ptwordfinder.commands.PTWordFinder import sanitize_pattern


def test_sanitize_pattern_with_allowed_characters():
    """
    Test sanitize_pattern function with a pattern containing
    allowed characters.

    Verifies that:
    - Allowed characters remain unchanged in the sanitized pattern.
    """
    original_pattern = "abc123[]()+*^$|. "
    sanitized_pattern = "abc123\\[\\]\\(\\)\\+\\*\\^\\$\\|\\.\\ "
    assert sanitize_pattern(original_pattern) == sanitized_pattern


def test_sanitize_pattern_simple():
    """
    Test sanitize_pattern function with a simple pattern.

    Verifies that:
    - The function correctly escapes special characters in the input pattern.
    """
    pattern = "example.pattern"
    expected_sanitized_pattern = r"example\.pattern"
    assert sanitize_pattern(pattern) == expected_sanitized_pattern


def test_sanitize_pattern_with_disallowed_characters():
    """
    Test sanitize_pattern function with a pattern containing
    disallowed characters.

    Verifies that:
    - Disallowed characters are escaped from the input string.
    """
    original_pattern = "abc123#@!()+*^$|. "
    sanitized_pattern = "abc123\#@!\\(\\)\\+\\*\\^\\$\\|\\.\\ "
    assert sanitize_pattern(original_pattern) == sanitized_pattern


def test_sanitize_pattern_with_empty_pattern():
    """
    Test sanitize_pattern function with an empty pattern.

    Verifies that:
    - An empty string input returns an empty string.
    """
    original_pattern = ""
    sanitized_pattern = ""
    assert sanitize_pattern(original_pattern) == sanitized_pattern


def test_no_special_characters():
    """
    Test sanitize_pattern function with a string
    containing no special characters.

    Verifies that:
    - The function returns the same string
    when the input has no special characters.
    """
    original_pattern = "simple_pattern"
    sanitized_pattern = "simple_pattern"
    assert sanitize_pattern(original_pattern) == sanitized_pattern


@pytest.mark.parametrize(
    "original_pattern, expected_sanitized_pattern",
    [
        ("special*characters", "special\\*characters"),
        ("^$()[]{}.*+?|\\", r"\^\$\(\)\[\]\{\}\.\*\+\?\|\\"),
        (r"\d+", "\\\\d\\+"),
        ("user-provided$pattern", "user\\-provided\\$pattern"),
        ("another^pattern", "another\\^pattern"),
    ],
)
def test_escape_metacharacters(original_pattern, expected_sanitized_pattern):
    """
    Test the sanitize_pattern function with various patterns.

    Args:
        original_pattern (str): The original pattern before sanitization.
        expected_sanitized_pattern (str): The expected sanitized pattern.

    Verifies that:
    Function are escaping of metacharacters:
    - Use two backslashes
    - Test with a pattern containing metacharacters
    - Raw string with escape
    - Dollar sign at the end
    - Caret at the beginning
    """
    sanitized_pattern = sanitize_pattern(original_pattern)
    assert sanitized_pattern == expected_sanitized_pattern


def test_sanitize_pattern_with_non_string_input():
    """
    Test sanitize_pattern function with non-string input.

    Verifies that:
    - Passing a non-string input raises a TypeError.
    """
    with pytest.raises(TypeError):
        sanitize_pattern(123)
