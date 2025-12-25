def min_min_max(arr):
    smallest = min(arr)
    largest = max(arr)
    values = set(arr)

    for num in range(smallest + 1, largest):
        if num not in values:
            return [smallest, num, largest]
