def count_bits(n):
    count = 0
    binary = bin(n)
    
    for i in binary:
        if i == "1":
            count += 1

    return count
