def mxdiflg(a1, a2):
    if len(a1) and len(a2) > 0: 
        a = abs(len(max(a1, key=len)) - len(min(a2, key=len))) 
        b = abs(len(max(a2, key=len)) - len(min(a1, key=len)))
        return b if b > a else a
    else:
        return -1
