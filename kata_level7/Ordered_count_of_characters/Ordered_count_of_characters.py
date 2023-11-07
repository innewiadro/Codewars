def ordered_count(inp):
    d = {}
    for i in inp:
        d[i] = d.get(i, 0) + 1

    return [(k, v) for k, v in d.items()]
