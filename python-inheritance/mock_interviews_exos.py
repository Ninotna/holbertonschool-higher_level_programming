def is_armstrong_number(number):
    """
    is_armstrong_number - Is a number an armstrong number
    """
    str_number= str(number)
    digits = len(str_number)

    sum = 0
    for digit in str_number:
        sum += int(digit) ** digits

    if sum == number:
        return 1
    return 0



def reverse_string(s):
    """
    reverse_string - Reverses the given string
    """
    return s[::-1]