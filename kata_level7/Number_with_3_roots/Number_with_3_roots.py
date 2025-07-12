def perfect_roots(n):
    r2 = n ** 0.5
    if r2 != int(r2):
        return False

    r4 = n ** 0.25
    if r4 != int(r4):
        return False

    r8 = n ** 0.125
    if r8 != int(r8):
        return False

    return True
