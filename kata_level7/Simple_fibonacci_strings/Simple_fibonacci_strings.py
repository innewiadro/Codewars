def solve(n):
    if n == 0:
        return "0"
    if n == 1:
        return "01"

    f = ["0", "01"]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]
