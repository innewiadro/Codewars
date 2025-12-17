def calc_tip(p, r):
    rounded_price = ((p + 5) // 10) * 10
    T = rounded_price // 10
    if r == 1:     
        T += 1
    elif r == 0:    
        T -= 1
    elif r == -1:      
        T = (T // 2) - 1
    return max(T, 0)
