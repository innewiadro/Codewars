def kebabize(st):
    a = []
    
    for i in st:
        if i.islower():
            a.append(i)
        elif i.isupper():
            a.append("-" + i.lower())
             
    if a == []:
        return ""
    if "-" in a[0]:
        a[0] = a[0][1:]
            
    return "".join(a)
