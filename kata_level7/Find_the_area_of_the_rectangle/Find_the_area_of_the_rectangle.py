import math


def area(d, l):
    if d <= l:
        return "Not a rectangle"

    other_side = math.sqrt(d ** 2 - l ** 2)
    res = l * other_side

    return round(res, 2)
