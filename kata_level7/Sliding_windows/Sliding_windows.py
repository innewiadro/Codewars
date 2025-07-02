def window(lngth, offst, lst):
    if lngth == 0:
        return [[] for _ in range(0, len(lst) + 1, offst)]

    return [lst[i:i + lngth] for i in range(0, len(lst) - lngth + 1, offst)]

