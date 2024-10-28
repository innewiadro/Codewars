def vampire_test(x, y):
    res = sorted(list(str(x)) + list(str(y)))
    res1 = sorted(list(str(x * y)))
    return res == res1
