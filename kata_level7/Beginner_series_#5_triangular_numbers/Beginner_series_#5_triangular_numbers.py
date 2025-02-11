def is_triangular(t):
    if t < 0:
        return False

    sum = 0
    i = 1

    while sum < t:
        sum += i
        if sum == t:
            return True

        i += 1
    return False
