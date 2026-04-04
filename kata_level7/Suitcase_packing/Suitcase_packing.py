def fit_in(a, b, m, n):
    return (max(a, b) <= m and a + b <= n) or (max(a, b) <= n and a + b <= m)
