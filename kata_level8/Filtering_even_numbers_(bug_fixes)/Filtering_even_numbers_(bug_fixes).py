def kata_13_december(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 2 == 0:
            lst.pop(i)
    return lst
