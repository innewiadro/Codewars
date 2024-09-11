def consecutive(arr):
    if not arr:
        return 0

    min_val = min(arr)
    max_val = max(arr)

    total_needed = max_val - min_val + 1

    return total_needed - len(arr)
