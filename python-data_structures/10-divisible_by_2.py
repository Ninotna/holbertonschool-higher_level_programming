def divisible_by_2(my_list=[]):
    """
    divisible_by_2 - finds all multiples of 2 in a list
    @my_list: the list of integers to check
    Return: a new list with True or False depending on whether each element is divisible by 2
    """
    result_list = []
    for num in my_list:
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
