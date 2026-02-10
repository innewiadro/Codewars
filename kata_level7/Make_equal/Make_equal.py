def count(a, t, x):
    if x == 0:
        return sum(1 for v in a if v == t)

    return sum(1 for v in a if (t - v) % x == 0)
