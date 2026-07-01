def moser():
    n = 1
    while True:
        yield 1 + (n * (n - 1)) // 2 + (n * (n - 1) * (n - 2) * (n - 3)) // 24
        n += 1