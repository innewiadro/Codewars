def digital_root(n):
    my_list = list(str(n))
    summ = 0
    for i in my_list:
        summ += int(i)
        print(summ)

    if summ > 9:
        return digital_root(summ)

    return summ
