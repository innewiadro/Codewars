def find_all(array, n):
    con = 0
    res = []
    for i in array:
        if i == n:
            res.append(con)
        con += 1
    return res
