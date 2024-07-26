def solve(arr):
    arr_sorted = sorted(arr)

    min_idx = 0
    max_idx = len(arr) - 1

    result = []

    toggle = True

    while min_idx <= max_idx:
        if toggle:
            result.append(arr_sorted[max_idx])
            max_idx -= 1
        else:
            result.append(arr_sorted[min_idx])
            min_idx += 1
        toggle = not toggle

    return result
