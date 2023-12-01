def cube_odd(arr):
    for i in arr:
        if isinstance(i, str):
            return None
        if isinstance(i, bool):
            return None

    return sum([i ** 3 for i in arr if i % 2 == 1])
