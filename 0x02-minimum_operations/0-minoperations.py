#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    func that calculates minimum number of operations
    needed to result in exactly n H

    Returns: an integer
            If n is impossible to achieve, returns 0
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    my_iterator = 2
    while (my_iterator <= n):
        if not (n % my_iterator):
            n = int(n / my_iterator)
            operations += my_iterator
            my_iterator = 1
        my_iterator += 1
    return operations
