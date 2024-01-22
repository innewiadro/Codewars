def bar_triang(point_a, point_b, point_c):
    return [round(sum(i) / 3, 4) for i in zip(point_a, point_b, point_c)]
