def find_digit(num, nth):
    if nth <= 0:
        return -1
    elif nth > len(str(abs(num))):
        return 0
    else:
        return int(str(abs(num))[::-1][nth-1])
