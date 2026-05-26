import math


def is_pronic(n):
    if n < 0:
        return False

    x = int(math.sqrt(n))
    return x * (x + 1) == n