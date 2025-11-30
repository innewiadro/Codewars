def next_numb(n):
    def has_unique_digits(x):
        s = str(x)
        return len(s) == len(set(s))

    n += 1
    limit = 9876543210
    while n <= limit:
        if n % 2 == 1:
            if n % 3 == 0:
                if has_unique_digits(n):
                    return n
        n += 1

    return "There is no possible number that fulfills those requirements"
