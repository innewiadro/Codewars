def arbitrate(inp):
    for i, c in enumerate(inp):
        if c == '1':
            return '0' * i + '1' + '0' * (len(inp) - i - 1)
    return '0' * len(inp)
