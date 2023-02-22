def series_sum(n):
    amount = 0
    for i in range(n):
        amount += (1 / (1 + i * 3))
    return str(format(sum, ".2f"))


def series_sum_list_comprehension(n):
    return format(sum((1 / (1 + i * 3)) for i in range(n)), ".2f")


