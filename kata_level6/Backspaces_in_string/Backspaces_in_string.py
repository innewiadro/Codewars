def clean_string(s):
    b = []
    for i in range(len(s)):
        b.append(s[i])
        if b[-1] == "#":
            try:
                b.pop()
                b.pop()
            except:
                continue
    return "".join(b)
