def last_digit(n1, n2):
    cycles = {
        0: [0, 0, 0, 0], 1: [1, 1, 1, 1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6, 4, 6],
        5: [5, 5, 5, 5], 6: [6, 6, 6, 6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1, 9, 1]}
    
    if n2 == 0:
        return 1
    else:
        last_digit_n1 = int(str(n1)[-1])
        lst_digit_list = cycles[last_digit_n1]
    return lst_digit_list[(n2 % 4) - 1]
