#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    roman_to_int - Converts a Roman numeral to an integer
    @roman_string: The Roman numeral string
    Return: The integer conversion, or 0 if input is invalid
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    length = len(roman_string)

    for i in range(length):
        # Check if the current value is smaller than the next one
        if i + 1 < length and roman_values[roman_string[i]] < roman_values[roman_string[i + 1]]:
            total -= roman_values[roman_string[i]]
        else:
            total += roman_values[roman_string[i]]

    return total
