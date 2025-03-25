def count_zeros(x):
    count = 0
    for num in range(1, x + 1):
        count += str(num).count('0')
    return count
