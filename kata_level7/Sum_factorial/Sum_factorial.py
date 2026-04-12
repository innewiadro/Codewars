def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sum_factorial(lst):
    total = 0
    for num in lst:
        total += factorial(num)
    return total
