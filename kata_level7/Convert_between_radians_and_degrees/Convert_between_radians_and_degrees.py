import math


def degrees(rad):
    deg = rad * (180 / math.pi)
    deg_str = f"{deg:.2f}".rstrip('0').rstrip('.')
    return f"{deg_str}deg"


def radians(deg):
    rad = deg * (math.pi / 180)
    rad_str = f"{rad:.2f}".rstrip('0').rstrip('.')
    return f"{rad_str}rad"
