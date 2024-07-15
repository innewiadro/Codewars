def extra_perfect(n: int) -> list[int] :
    res = []
    for i in range(1, n+1, 2):
        res.append(i)
    return res
