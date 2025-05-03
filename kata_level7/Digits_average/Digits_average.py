import math


def digits_average(x):
    digits = [int(d) for d in str(x)]

    while len(digits) > 1:
        digits = [math.ceil((digits[i] + digits[i + 1]) / 2) for i in range(len(digits) - 1)]

    return digits[0]
