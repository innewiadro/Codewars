def f(p, q):
    if p == 0 and q == 0:
        return None

    a_first = p / (1 - (1 - p) * (1 - q))
    b_first = (1 - q) * a_first

    return (a_first, b_first)
