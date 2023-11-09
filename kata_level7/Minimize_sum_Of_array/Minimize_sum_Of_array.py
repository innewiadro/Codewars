def min_sum(arr):
    list_top = []
    list_bottom = []
    srt = sorted(arr)
    rev = sorted(arr, reverse=True)
    res = 0

    for i in range(0, int(len(arr) / 2)):
        list_top.append(srt[i])
        list_bottom.append(rev[i])

    for i, j in zip(list_bottom, list_top):
        res += i * j

    return res