from itertools import accumulate


def spacey(array):
    b = accumulate(array)
    return list(b)
