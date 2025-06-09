def magic_sum(arr):
    return sum(num for num in arr if num % 2 == 1 and '3' in str(abs(num)))
