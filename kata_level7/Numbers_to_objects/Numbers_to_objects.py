def num_obj(s):
    res = []
    for i in s:
        add = {}
        add[str(i)] = chr(i)
        res.append(add)
    return res
