from math import gcd
from math import lcm


def merge_ratios(r1, r2):
    a, b1 = map(int, r1.split(':'))
    b2, c = map(int, r2.split(':'))

    common = lcm(b1, b2)

    mul1 = common // b1
    mul2 = common // b2

    A = a * mul1
    B = common
    C = c * mul2

    g = gcd(gcd(A, B), C)

    return f"{A // g}:{B // g}:{C // g}"
