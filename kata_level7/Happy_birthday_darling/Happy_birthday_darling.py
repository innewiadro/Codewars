def womens_age(n):
    if n % 2 == 0:
        base = n // 2
        return f"{n}? That's just 20, in base {base}!"
    else:
        base = (n - 1) // 2
        return f"{n}? That's just 21, in base {base}!"