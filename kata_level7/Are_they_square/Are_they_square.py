import math


def is_square(arr):
    if not arr:
        return None

    return all(math.isqrt(x) ** 2 == x for x in arr)
