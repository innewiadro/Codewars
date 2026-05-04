def find_middle(s):
    if not isinstance(s, str):
        return -1

    digits = [int(c) for c in s if c.isdigit()]
    if not digits:
        return -1

    from math import prod
    p = str(prod(digits))
    mid = len(p) // 2

    return int(p[mid]) if len(p) % 2 else int(p[mid-1:mid+1])