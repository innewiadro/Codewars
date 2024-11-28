def diagonal_sum(array):
    res = 0
    a = len(array[0])

    for i in range(a):
        res += array[i][i]

    return res
