def skiponacci(n):
    if n == 1:
        return "1"

    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    result = [
        str(fib[i]) if i % 2 == 0 else "skip"
        for i in range(n)
    ]
    return " ".join(result)
