def check_character(text: str, char: str) -> int:

    count = 0


    for c in text:
        if c == char:
            count += 1

    return count



print(check_character("Ahoj jak to jde", "A"))  # Output: 2