#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    weight_average - Returns the weighted average of all integers in tuple
    @my_list: List of tuples (<score>, <weight>)
    Return: The weighted average, or 0 if the list is empty
    """
    if not my_list:
        return 0

    numerator = sum(score * weight for score, weight in my_list)
    denominator = sum(weight for score, weight in my_list)

    return numerator / denominator if denominator != 0 else 0
