def pattern(n):
    if n <= 0:
        return ""

    res = []

    for i in range(1, n + 1):
        line = "".join(str(j) for j in range(i, n + 1))
        res.append(line)

    return "\n".join(res)
