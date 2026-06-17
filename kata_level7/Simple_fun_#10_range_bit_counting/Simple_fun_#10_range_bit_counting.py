def range_bit_count(a, b):
    total = 0
    for num in range(a, b + 1):
        total += bin(num).count('1')
    return total
