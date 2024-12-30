from collections import Counter

def odd_ones_out(numbers):
    counts = Counter(numbers)
    return [num for num in numbers if counts[num] % 2 == 0]
