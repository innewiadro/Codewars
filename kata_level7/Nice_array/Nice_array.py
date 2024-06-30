def is_nice(arr):
    if len(arr) == 0:
        return False
    for i in arr:
        if (i + 1) in arr:
            continue
        elif (i - 1) in arr:
            continue
        else:
            return False
    return True
