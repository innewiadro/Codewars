def largest_pair_sum(numbers): 
    a = sorted(numbers)
    return a[-1] + a[-2]
