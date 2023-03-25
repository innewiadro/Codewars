from math import log, sqrt


def isPP(n):
    the_bigest_sqrt = int(sqrt(n))
    for i in range(2, the_bigest_sqrt + 1):
        k = int(round(log(n, i)))
        if i ** k == n:
            return [i, k]
    return None
