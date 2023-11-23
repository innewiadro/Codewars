def max_tri_sum(numbers):
    s = sorted(set(numbers))
    return sum(s[-3:])
