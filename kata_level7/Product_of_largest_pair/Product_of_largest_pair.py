def max_product(a):
    max_num1 = max(a)
    a.remove(max_num1)
    return max_num1 * max(a)
