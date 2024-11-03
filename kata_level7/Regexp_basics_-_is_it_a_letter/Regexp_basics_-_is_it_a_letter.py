def is_letter(s):
    return isinstance(s, str) and len(s) == 1 and s.isalpha() and s.isascii()