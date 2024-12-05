def reverse(n):
    result = 0
    is_negative = n < 0
    n = abs(n)

    while n > 0:
        remainder = n % 10
        result = result * 10 + remainder
        n //= 10

    return -result if is_negative else result
