"""
A module for testing the `_is_valid_number` function from the `study_io` module.

The module contains multiple test cases for the `_is_valid_number` function.
Each test case checks a different scenario, such as valid and invalid numbers,
empty strings, and negative numbers.

The test cases use the `_is_valid_number` function from the `study_io` module to perform the check.
The function takes a number as input and checks if it is a valid number.
It returns `True` if the number is valid, and `False` otherwise.

Test Cases:
- `test_is_valid_number_with_valid_number`
    - Tests if a given number is valid.
- `test_is_valid_number_with_invalid_number`
    - Tests if the function correctly identifies an invalid number.
- `test_is_valid_number_with_empty_string`
    - Tests if the function returns `False` when an empty string is passed.
- `test_is_valid_number_with_negative_number`
    - Tests the function with a negative number.

Parameters:
    None

Returns:
    None
"""
# DEPENDENCIES
## App
from ..components.study_io import _is_valid_number


# TESTS
## __is_valid_number
def test_is_valid_number_with_valid_number() -> None:
    """
    A function to test if a given number is valid.
    This function takes a number as input and checks if it is a valid number.
    It uses the `_is_valid_number` method from the `study_io` module to perform the check.
    Parameters:
        - number: The number to be checked (type: str)
    Returns:
        - True if the number is valid, False otherwise (type: bool)
    """
    assert _is_valid_number("12345") is True

def test_is_valid_number_with_invalid_number() -> None:
    """
    Test case for the `study_io._is_valid_number` function.
    This test case checks whether the function correctly identifies an invalid number.
    Parameters:
        None
    Returns:
        None
    """
    assert _is_valid_number("abcde") is False

def test_is_valid_number_with_empty_string() -> None:
    """
    Test case for the `test_empty_string` function.
    It asserts that the `_is_valid_number` function from the `study_io` module
    returns `False` when an empty string is passed as a parameter.
    """
    assert _is_valid_number("") is False

def test_is_valid_number_with_negative_number() -> None:
    """
    Test the function _is_valid_number() in the study_io module with a negative number.
    """
    assert _is_valid_number("-123") is False
