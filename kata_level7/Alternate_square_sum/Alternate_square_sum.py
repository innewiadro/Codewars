def alternate_sq_sum(arr):
    if not arr:
        return 0
    return sum(x**2 if i % 2 == 1 else x for i, x in enumerate(arr))
