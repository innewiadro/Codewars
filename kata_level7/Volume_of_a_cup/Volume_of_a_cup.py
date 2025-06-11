import math


def cup_volume(r1, r2, height):
    r1 = r1 / 2
    r2 = r2 / 2
    return (1 / 3) * math.pi * height * (r1**2 + r1 * r2 + r2**2)
