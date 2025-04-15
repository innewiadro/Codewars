import math


def sort_by_area(seq):
    def area(shape):
        if isinstance(shape, tuple):
            return shape[0] * shape[1]
        else:
            return math.pi * shape ** 2

    return sorted(seq, key=area)
