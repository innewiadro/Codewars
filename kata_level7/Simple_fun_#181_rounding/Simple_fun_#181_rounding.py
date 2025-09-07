def rounding(n, m):
    lower = (n // m) * m
    upper = ((n + m - 1) // m) * m

    if n - lower == upper - n:
        return n
    elif n - lower < upper - n:
        return lower
    else:
        return upper
