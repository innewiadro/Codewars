def next_id(arr):
    used = set(arr)
    i = 0
    while i in used:
        i += 1
    return i