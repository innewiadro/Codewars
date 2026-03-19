import math


def calculate_ratio(w, h):
    if w == 0 or h == 0:
        raise ValueError("Width and height must be non-zero")

    gcd = math.gcd(w, h)

    w = w // gcd
    h = h // gcd

    return f"{w}:{h}"