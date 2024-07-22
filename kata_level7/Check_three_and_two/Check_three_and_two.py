def check_three_and_two(array):
    counts = {}
    for char in array:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
        res = list(counts.values())
    return sorted(res) == [2, 3]
