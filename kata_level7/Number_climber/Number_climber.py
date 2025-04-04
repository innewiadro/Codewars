def climb(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n - 1) // 2
    return sequence[::-1]
