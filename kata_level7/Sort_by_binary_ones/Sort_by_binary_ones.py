def sort_by_binary_ones (numList):
    return sorted(numList, key=lambda n:(-bin(n).count('1'), len(bin(n)) - 2,n ))