def pythagorean_triple(integers):
    max_val = max(integers)
    integers.remove(max_val)
    return max_val**2 == min(integers)**2 + max(integers)**2
