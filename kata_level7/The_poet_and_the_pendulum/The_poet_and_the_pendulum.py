def pendulum(arr):
    sorted_arr = sorted(arr)

    result = []

    for i, val in enumerate(sorted_arr):
        if i % 2 == 0:
            result.insert(0, val)
        else:
            result.append(val)

    return result
