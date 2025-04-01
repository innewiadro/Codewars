def score(n):
    if n == 0:
        return 0

    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8

    return n
