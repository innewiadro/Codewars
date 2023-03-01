def sum_dig_pow(a, b):
    d = []

    for i in range(a, b+1):
        c = []
        n = 0
        for j in str(i):
            c.append(int(j) ** (n+1))
            n += 1

        if i == sum(c):
            d.append(i)

    return d
