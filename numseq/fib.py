"""This function will return the fibonacci number
in the nth sequence of the pattern."""


def fib(n):
    """Returns fibonacci number at nth spot of the pattern"""
    a = 0
    b = 1
    for f in range(2, n):
        a = f + b
        b = f
    return a
