def collinearity(x1, y1, x2, y2):
    if (x1, y1) == (0, 0) or (x2, y2) == (0, 0):
        return True

    return x1 * y2 == x2 * y1
