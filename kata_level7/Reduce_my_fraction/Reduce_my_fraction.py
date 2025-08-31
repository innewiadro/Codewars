from math import gcd


def reduce_fraction(fraction):
    numerator, denominator = fraction
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor
