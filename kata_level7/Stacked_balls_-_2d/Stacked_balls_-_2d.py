import math


def stack_height_2d(n):
    if n == 0:
        return 0
    return 1 + (n - 1) * (math.sqrt(3) / 2)
