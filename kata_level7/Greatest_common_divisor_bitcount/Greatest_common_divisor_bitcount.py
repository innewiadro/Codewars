import math


def binary_gcd(a, b):
    if a == 0 and b == 0:
        return 0
    gcd = math.gcd(abs(a), abs(b))
    return bin(gcd).count('1')
