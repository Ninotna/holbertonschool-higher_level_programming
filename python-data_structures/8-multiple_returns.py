#!/usr/bin/python3

def multiple_returns(sentence):
    """
    multiple_returns - returns a tuple with the length of a string and its first character
    @sentence: the string to evaluate
    Return: a tuple (length of sentence, first character or None if empty)
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
