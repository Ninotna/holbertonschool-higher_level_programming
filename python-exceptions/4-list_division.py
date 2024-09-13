#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    list_division - Divides element by element two lists
    @my_list_1: The first list
    @my_list_2: The second list
    @list_length: The length of the result list
    Return: A new list with the division results
    """
    new_list = []
    for i in range(list_length):
        try:
            # Try to perform the division
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            # Handle if elements are not numbers
            print("wrong type")
            result = 0
        except IndexError:
            # Handle if the index is out of range for either list
            print("out of range")
            result = 0
        finally:
            # Append the result to the new list
            new_list.append(result)
    return new_list
