def complete(st):
    for i in range(1, len(st) + 1):
        suffix = st[i:]
        if suffix == suffix[::-1]:
            return st + st[:i][::-1]