def odd_or_even(arr):
    sum_of_arr = 0
    for i in arr:
        sum_of_arr += i
    if sum_of_arr % 2 == 0 or sum_of_arr == 0:
        return "even"
    else:
        return "odd"
