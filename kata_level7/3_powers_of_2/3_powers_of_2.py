def three_powers(n):
    if n > 2:
        return bin(n).count('1') <= 3
    return False

