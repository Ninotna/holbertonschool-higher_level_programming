#!/usr/bin/python3

"""
Search and update
"""

def append_after(filename="", search_string="", new_string=""):
    """
    append_after - Inserts a line of text after each line containing 
    a specific string in a file.

    @filename: The name of the file to modify
    @search_string: The string to search for in each line
    @new_string: The string to insert after lines containing the search_string

    Return: None
    """
    # Open the file and read its lines
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Open the file again in write mode to overwrite it with modifications
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)  # Write the current line
            # If the line contains the search_string, append the new_string
            if search_string in line:
                file.write(new_string)
