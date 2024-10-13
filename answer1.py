def check_character(text: str, char: str) -> int:
    """
    This function returns the number of occurrences of 'char' in 'text' using a loop.
    """
    # Initialize a counter
    count = 0

    # Iterate through each character in the string
    for c in text:
        # If the current character matches the target character, increment the counter
        if c == char:
            count += 1

    return count



print(check_character("hello world", "o"))  # Output: 2