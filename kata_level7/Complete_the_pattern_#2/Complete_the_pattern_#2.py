def pattern(n):
    if n < 1:
        return ""

    result = []

    for i in range(n):
        row = ""
        for j in range(n, i, -1):
            row += str(j)
        result.append(row)

    return "\n".join(result)
