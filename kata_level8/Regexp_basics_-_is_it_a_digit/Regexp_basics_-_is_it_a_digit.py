def is_digit(n):
    return isinstance(n, str) and len(n) == 1 and n.isdigit()
