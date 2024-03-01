def max_gap(numbers):
    a = sorted(numbers, reverse=True)
    b = 0
    for i in range(len(a)-1):
        if a[i] - a[i+1] > b:
            b = a[i] - a[i+1]
    return b
