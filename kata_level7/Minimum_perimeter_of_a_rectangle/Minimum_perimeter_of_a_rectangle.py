import math


def minimum_perimeter(area):
    h = int(math.sqrt(area))

    while area % h != 0:
        h -= 1

    w = area // h
    return 2 * (h + w)
