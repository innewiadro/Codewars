def group_by_commas(n):
    a = []
    n_str = str(n)[::-1]
    for i in range(0, len(n_str), 3):
        a.append(n_str[i:i+3][::-1])
    a.reverse()    
    return ",".join(a)
