import math

def round_to_five(arr):
    return [math.floor(x / 5 + 0.5) * 5 for x in arr]