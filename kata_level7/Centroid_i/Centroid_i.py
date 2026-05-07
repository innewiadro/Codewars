def centroid(points: list[list[float]]) -> list[float]:
    if len(points) == 0:
        raise ValueError("The list of points cannot be empty")

    n = len(points)

    sum_x = sum(p[0] for p in points)
    sum_y = sum(p[1] for p in points)
    sum_z = sum(p[2] for p in points)

    return [sum_x / n, sum_y / n, sum_z / n]
