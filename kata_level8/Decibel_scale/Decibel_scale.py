import math


def db_scale(intensity):
    I0 = 10 ** -12
    beta = 10 * math.log10(intensity / I0)
    return beta
