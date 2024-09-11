def add_tuple(tuple_a=(), tuple_b=()):
    """
    add_tuple - adds 2 tuples and returns a tuple with 2 integers
    @tuple_a: first tuple
    @tuple_b: second tuple
    Return: a new tuple with the sum of the first and second elements of both tuples
    """
    # Ensure both tuples have at least two elements, using 0 for missing values
    tuple_a = (tuple_a + (0, 0))[:2]
    tuple_b = (tuple_b + (0, 0))[:2]

    # Add the first and second elements of both tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    
    return result
