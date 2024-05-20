
def reverse_bits(n):
    return int(bin(n).replace("0b", "")[::-1], 2)
