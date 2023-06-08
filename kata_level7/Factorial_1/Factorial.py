def factorial(n):
    fact = 1
    if n > 0 and n <= 12:
        for i in range(2, n + 1):
            fact *= i

        return fact
    elif n == 0:
        return 1
    else:
        raise ValueError
