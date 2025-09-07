def pattern(n: int) -> str:
    if n <= 0:
        return ""
    if n % 2 == 0:
        n -= 1

    rows = []
    for i in range(1, n + 1, 2):
        rows.append(str(i) * i)

    return "\n".join(rows)
