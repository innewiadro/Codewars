def complete_series(arr): 
    if len(arr) != len(set(arr)):
        return [0]

    return list(range(max(arr) + 1))
