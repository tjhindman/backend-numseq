"""Determines whether or not a number is prime."""


def is_prime(n):
    """Returns boolean based on if n is prime."""
    if n >= 2:
        for x in range(2, n):
            if not n % x:
                return False
    else:
        return True
    return True


def prime(n):
    """Returns list of prime numbers less than n."""
    p_list = [x for x in range(n) if is_prime(x)]
    return p_list
