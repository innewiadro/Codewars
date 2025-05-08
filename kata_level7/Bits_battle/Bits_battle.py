def bits_battle(numbers):
    odd_ones = 0
    even_zeros = 0

    for num in numbers:
        if num == 0:
            continue
        binary = bin(num)[2:]
        if num % 2 == 1:
            odd_ones += binary.count('1')
        else:
            even_zeros += binary.count('0')

    if odd_ones > even_zeros:
        return "odds win"
    elif even_zeros > odd_ones:
        return "evens win"
    else:
        return "tie"
