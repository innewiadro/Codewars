def powers(n):
    result = []
    power = 0
    while n > 0:
        if n & 1:
            result.append(2 ** power)
        power += 1
        n >>= 1
    return result
