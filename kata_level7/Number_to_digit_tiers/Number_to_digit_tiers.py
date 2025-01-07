import math


def create_array_of_tiers(n):
    res = []
    for i in range(len(str(n))):
        res.append(str(math.floor(n / 10**i)))
    return res[::-1]
