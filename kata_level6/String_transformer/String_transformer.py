def string_transformer(s):
    a = []
    b = s.split(" ", maxsplit=-1)
    b.reverse()
    s = " ".join(b)
    for i in s:
        if i.islower():
            a.append(i.upper())
        elif i.isupper():
            a.append(i.lower())
        else:
            a.append(i)
        
    return "".join(a)
