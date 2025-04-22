def eq_sum_powdig(h_max, exp):
    result = []
    for num in range(2, h_max + 1):
        digits = [int(d) for d in str(num)]
        if sum(d ** exp for d in digits) == num:
            result.append(num)
    return result
