def even_chars(st):
    print(st)
    return list(st[1::2]) if 1 < len(st) < 100 else 'invalid string'

