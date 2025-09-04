import math

def triangle_perimeter(triangle):
    def distance(p1, p2):
        return math.hypot(p1.x - p2.x, p1.y - p2.y)

    return (distance(triangle.a, triangle.b) +
            distance(triangle.b, triangle.c) +
            distance(triangle.c, triangle.a))
