def calculate_total(t1, t2):
    t1s = sum(x or 0 for x in t1)
    t2s = sum(x or 0 for x in t2)
    return t1s > t2s
