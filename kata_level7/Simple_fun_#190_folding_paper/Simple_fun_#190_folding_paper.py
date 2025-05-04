def folding(a, b):
    count = 0
    while b:
        count += a // b
        a, b = b, a % b
    return count