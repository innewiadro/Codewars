from collections import Counter

def solve(a, b):
    counter = Counter(a)
    return [counter[word] for word in b]