def max_product(lst, n_largest_elements):
    b = sorted(lst, reverse=True)[0:n_largest_elements]
    result = 1
    for x in b:
        result = result * x
    return result
