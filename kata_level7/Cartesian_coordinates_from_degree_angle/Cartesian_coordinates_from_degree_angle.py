import math


def coordinates(degrees: float, radius: float) -> tuple[float, float]:
    x = radius * math.cos(math.radians(degrees))
    y = radius * math.sin(math.radians(degrees))
    return x, y
