def get_last_digit(n):
    if n <= 1:
        return n

    n %= 60

    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10

    return curr
