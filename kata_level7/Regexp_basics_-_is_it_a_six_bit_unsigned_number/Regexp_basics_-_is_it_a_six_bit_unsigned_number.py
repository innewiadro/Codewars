import re


def six_bit_number(n):
    if not re.fullmatch(r'(0|[1-9][0-9]*)', n):
        return False
    num = int(n)
    return 0 <= num <= 63
