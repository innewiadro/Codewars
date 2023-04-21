def reverse_alternate(s):
    a = s.split()
    b = []
    for i in range(len(a)):
        if i % 2 == 0:
            b.append(a[i])
        else:
            c = a[i][::-1]
            b.append(c)
    
    return " ".join(b)
