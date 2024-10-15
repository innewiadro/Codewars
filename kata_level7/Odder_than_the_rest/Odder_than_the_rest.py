def odd_one(arr):
    for i, num in enumerate(arr):
        if num % 2 != 0:  # Check if the number is odd
            return i
    return -1
