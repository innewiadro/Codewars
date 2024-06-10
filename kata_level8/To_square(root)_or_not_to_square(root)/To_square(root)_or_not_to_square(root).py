def square_or_square_root(arr):
    return [int(i**0.5) if i**0.5 % 1 == 0 else i**2 for i in arr]
