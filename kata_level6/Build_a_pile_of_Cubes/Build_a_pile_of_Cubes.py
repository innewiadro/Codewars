def find_nb(m):
    base = 1
    my_summ_of_exponent = 0
    while my_summ_of_exponent <= m:
        my_summ_of_exponent += base ** 3
        
        if my_summ_of_exponent == m:
            return base
        base += 1
    return -1
