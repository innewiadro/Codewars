def sxore(n):
    r = n % 4
    if r == 0:
        return n
    elif r == 1:
        return 1
    elif r == 2:
        return n + 1
    else:
        return 0
