"""
This module defines classes and functions related to sound and CLI input/output.
"""
# HELPER FUNCTIONS
## Error Handling
def _is_valid_number(string_input: str) -> bool:
    """
    Check if the given string is a valid number.

    Parameters:
        string_input (str): The string to be evaluated.

    Returns:
        bool: True if the string is a valid number, False otherwise.
    """
    if string_input.isdigit():
        return True
    print("Please enter a valid number")
    return False

# INPUT
def get_study_length() -> int:
    """
    Get the length of a study session from user.

    Returns:
        int: The length of the study session in minutes.

    Raises:
        ValueError: If the entered study length is not a valid number or is less than 15 minutes.
    """
    while True:
        study_length = input("How long is your study session in minutes?\n")
        if not _is_valid_number(study_length):
            continue
        study_length = int(study_length)
        # Make sure amount is valid
        if study_length < 5:
            print("Time must be more than 5 minutes")
            continue
        break
    return study_length


# OUTPUT
def immediate_print(text: str) -> None:
    """
    Print the given text immediately to the console.

    Args:
        text (str): The text to be printed.

    Returns:
        NoReturn: This function does not return anything.
    """
    print(text, end="\r", flush=True)
