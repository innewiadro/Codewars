def sum_of_n(n):
    a = 0
    nw_list = []
    z = 1
    x = n + 1
    if n < 0:
        z = - 1
        x = n - 1
    for i in range(0, x, z):
        a = a + i
        nw_list.append(a)
    return nw_list
