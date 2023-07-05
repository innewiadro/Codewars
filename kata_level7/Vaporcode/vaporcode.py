def vaporcode(s):
    a = ""
    for i in s:
        if i == " ":
            continue
        else:
            a += i.upper() + "  "       
    return a[:-2]
