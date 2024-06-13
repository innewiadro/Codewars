def symmetric_point(p, q):
    x1, y1 = p
    x2, y2 = q
    x3 = 2 * x2 - x1
    y3 = 2 * y2 - y1
    return [x3, y3]
