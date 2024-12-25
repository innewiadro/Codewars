def prev_mult_of_three(n):
    if n % 3 == 0:
        return n

    while n > 0:
        n //= 10
        if n % 3 == 0 and n != 0:
            return n
