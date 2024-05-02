def nth_fib(n):
    if n == 1:
        return 0

    fib = [0, 1]
    for i in range(n - 2):
        fib.append(sum(fib[-2:]))

    return fib[-1]
