def div_con(x):
    sum_int = 0
    sum_str = 0

    for i in x:
        if isinstance(i, int):
            sum_int += i
        else:
            sum_str += int(i)

    return sum_int - sum_str
