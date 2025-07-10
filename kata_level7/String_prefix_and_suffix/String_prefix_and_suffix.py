def solve(st):
    n = len(st)
    for k in range(n // 2, 0, -1):
        if st[:k] == st[-k:]:
            return k
    return 0
