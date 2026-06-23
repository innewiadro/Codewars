def smallest_transform(num):
    digits = [int(d) for d in str(num)]

    best = float('inf')

    for t in range(10):
        cost = sum(abs(d - t) for d in digits)
        best = min(best, cost)

    return best