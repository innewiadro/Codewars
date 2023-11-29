def sum_of_minimums(numbers):
    lowest_sum = 0

    for i in numbers:
        lowest_sum += min(i)

    return lowest_sum
