import math


def round_it(n):
    parts = str(n).split('.')
    left_length = len(parts[0])
    right_length = len(parts[1])

    if left_length < right_length:
        return math.ceil(n)
    elif left_length > right_length:
        return math.floor(n)
    else:
        return round(n)
