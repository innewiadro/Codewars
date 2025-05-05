import math


def content_weight(bottle_weight, scale):
    num, _, direction = scale.split()
    multiplier = int(num)

    if direction == "larger":
        x = bottle_weight / (1 + multiplier)
        return int(multiplier * x)
    elif direction == "smaller":
        x = bottle_weight / (1 + 1 / multiplier)
        return round(x / multiplier)
