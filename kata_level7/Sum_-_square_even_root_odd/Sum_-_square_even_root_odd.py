import math

def sum_square_even_root_odd(nums):
    return round(sum(math.sqrt(x) if x % 2 != 0 else x ** 2 for x in nums), 2)