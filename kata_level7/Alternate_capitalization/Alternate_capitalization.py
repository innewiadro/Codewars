def capitalize(s):
    a = "".join([s[i].upper() if i % 2 == 0 else s[i].lower() for i in range(len(s))])
    b = "".join([s[i].upper() if i % 2 != 0 else s[i].lower() for i in range(len(s))])       
    return [a, b]
