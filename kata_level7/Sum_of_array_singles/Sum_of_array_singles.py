from collections import Counter


def repeats(arr):
    return sum(num for num, count in Counter(arr).items() if count == 1)
