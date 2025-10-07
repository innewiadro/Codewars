def euclidean_distance(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions.")

    squared_diff = sum((a - b) ** 2 for a, b in zip(point1, point2))
    return round(squared_diff ** 0.5, 2)
