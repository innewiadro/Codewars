def solve(st,a,b):
    b = min(b, len(st) - 1)
    return st[:a] + st[a:b+1][::-1] + st[b+1:]
