def find_slope(points):
    a, b, c, d = points

    if a == c:
        return "undefined"

    slope = (d - b) // (c - a)
    return str(slope)
