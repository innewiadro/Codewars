def compound_array(a, b):
    res = []
    length = max(len(a), len(b))

    for i in range(length):
        if i < len(a):
            res.append(a[i])
        if i < len(b):
            res.append(b[i])

    return res
