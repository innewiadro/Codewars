from collections import Counter


def is_zero_balanced(arr):
    if not arr or sum(arr) != 0:
        return False

    counts = Counter(arr)
    for num in counts:
        if counts[num] != counts[-num]:
            return False

    return True
