import math


def new_avg(arr, newavg):
    current_sum = sum(arr)
    target_sum = (len(arr) + 1) * newavg
    next_donation = target_sum - current_sum

    if next_donation <= 0:
        raise ValueError("Expected donation must be greater than 0.")

    return math.ceil(next_donation)
