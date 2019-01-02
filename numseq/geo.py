"""Returns a number that has either been
squared, cubed, or a triangle."""


def sqr(n):
    """Returns square of n."""
    s = n ** 2
    return s


def cube(n):
    """Returns cube of n."""
    c = n ** 3
    return c


def tri(n):
    """Returns area of equilateral triangle."""
    sq = sqr(n)
    tri = sq / 2
    return tri
