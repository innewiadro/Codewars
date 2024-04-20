def create_dict(keys, values):
    res = {}
    while len(keys) > len(values):
        values.append(None)
    for key in keys:
        for value in values:
            res[key] = value
            values.remove(value)
            break
    return res
