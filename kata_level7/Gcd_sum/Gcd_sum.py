from math import gcd


def solve(s, g):
    if s % g != 0:
        return -1

    k = s // g

    for x in range(1, k):
        y = k - x
        if gcd(x, y) == 1:
            a = x * g
            b = y * g
            return (min(a, b), max(a, b))
