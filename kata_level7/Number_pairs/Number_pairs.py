def get_larger_numbers(a, b):
    res = []
    for i in range(len(a)):
        if a[i] >= b[i]:
            res.append(a[i])
        else:
            res.append(b[i])
    return res
