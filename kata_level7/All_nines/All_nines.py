def all_nines(x):
    if x % 2 == 0 or x % 5 == 0:
        return -1

    remainder = 0
    for length in range(1, 100_000):
        remainder = (remainder * 10 + 9) % x
        if remainder == 0:
            nine_number = int("9" * length)
            return nine_number // x
    return -1
