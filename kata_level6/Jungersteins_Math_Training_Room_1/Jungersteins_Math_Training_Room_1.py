def count_zeros_n_double_fact(n):
    multiply = 1
    if n % 2 == 0:
        for digit in range(2, n + 1, 2):
            print(digit)
            multiply = multiply * digit

    i = 1
    while multiply % (10 ** i) == 0:
        i += 1

    return 0 if i == 1 else i - 1
