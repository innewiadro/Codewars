def minimum_percentage(foods):
    total = sum(foods)
    n = len(foods)
    return max(0, total - 100 * (n - 1))
