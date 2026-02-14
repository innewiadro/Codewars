def pattern(n):
    if n < 1:
        return ""

    rows = []
    for i in range(1, n + 1):
        rows.append(str(i) * i)

    return "\n".join(rows)