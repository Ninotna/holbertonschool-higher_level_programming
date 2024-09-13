#!/usr/bin/python3
def best_score(a_dictionary):
    """
    best_score - Returns the key with the biggest integer value
    @a_dictionary: The input dictionary where values are integers
    Return: The key with the highest value, or None if the dictionary is empty
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
