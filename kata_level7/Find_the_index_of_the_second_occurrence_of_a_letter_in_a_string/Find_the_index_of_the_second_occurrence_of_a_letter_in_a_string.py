def second_symbol(s, symbol):
    a = 0
    b = -1
    for i in s:
        b += 1
        if i == symbol:
            a += 1
        if a > 1:
            return b
    return b if a > 1 else -1
