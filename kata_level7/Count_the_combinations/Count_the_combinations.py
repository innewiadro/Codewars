from itertools import combinations

def num_combo(xs, n):
    count = 0
    size = len(xs)
    for idx_combo in combinations(range(size), size - 1):
        total = sum(xs[i] for i in idx_combo)
        if total == n:
            count += 1
    return count
