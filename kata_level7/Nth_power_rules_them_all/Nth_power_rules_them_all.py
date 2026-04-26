def modified_sum(arr, n):
    return sum(x**n for x in arr) - sum(arr)