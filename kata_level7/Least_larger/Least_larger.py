def least_larger(a, i):
    target = a[i]
    candidates = [(idx, num) for idx, num in enumerate(a) if num > target]
    if not candidates:
        return -1
    return min(candidates, key=lambda x: x[1])[0]