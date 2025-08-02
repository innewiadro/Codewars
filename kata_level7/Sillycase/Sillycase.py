def sillycase(s):
    mid = (len(s) + 1) // 2
    return s[:mid].lower() + s[mid:].upper()
