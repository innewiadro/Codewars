from math import prod


def sum_or_product(arr, n):
    largest_sum = sum(sorted(arr, reverse=True)[:n])
    smallest_product = prod(sorted(arr)[:n])

    if largest_sum > smallest_product:
        return "sum"
    elif smallest_product > largest_sum:
        return "product"
    else:
        return "same"
