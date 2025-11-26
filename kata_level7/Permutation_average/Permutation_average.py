def permutation_average(n):
    digits = list(map(int, str(n)))
    k = len(digits)
    place_value_sum = sum(10 ** i for i in range(k))
    total = sum(digits) * place_value_sum
    avg = total / k
    return round(avg)
