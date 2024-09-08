def is_very_even_number(n):
    if n < 10:
        return n % 2 == 0
    else:
        digit_sum = sum(int(digit) for digit in str(n))

    return is_very_even_number(digit_sum)
