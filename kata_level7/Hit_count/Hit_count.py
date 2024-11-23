def counter_effect(hit_count):
    last = []
    for i in hit_count:
        res = []
        for j in range(int(i)+1):
            res.append(j)
        last.append(res)
    return last
