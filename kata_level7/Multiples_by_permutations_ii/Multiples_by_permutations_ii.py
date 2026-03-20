from collections import Counter


def find_lowest_int(k):
    n = 1
    while True:
        a = n * k
        b = n * (k + 1)

        if Counter(str(a)) == Counter(str(b)):
            return n

        n += 1