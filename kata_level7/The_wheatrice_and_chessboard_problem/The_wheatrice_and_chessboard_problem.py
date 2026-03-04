import math


def squares_needed(grains):
    if grains == 0:
        return 0
    return math.ceil(math.log2(grains + 1))
