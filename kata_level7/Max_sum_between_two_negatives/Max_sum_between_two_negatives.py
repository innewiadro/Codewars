def max_sum_between_two_negatives(arr):
    list_of_max= []
    maximum = 0
    first_neg = False
    for i, num in enumerate(arr):
        if num < 0:
            if first_neg:
                list_of_max.append(maximum)
            else:
                first_neg = True
            maximum = 0
        else:
            maximum += num
    return max(list_of_max) if len(list_of_max) else -1

