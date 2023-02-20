def get_sum(a, b):
    c = 0

    if a < b:
        for i in range(a, b + 1):
            print(i)
            c += i

    else:
        for i in range(b, a+1):
            print(i)
            c += i

    return c
