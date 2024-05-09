def solve(arr):
    res = []
    for i in arr[::-1]:
        if i not in res:
            res.append(i)
    return res[::-1]
