def race(v1, v2, g):

    if v1 >= 0 and v2 > v1: 
        t = g / (v2/3600 - v1/3600)
        ms = t % 3600 % 60 % 1
        
        if ms > 0.99:
            t += 1
            
        h = round(t // 3600)
        m = t % 3600 // 60
        s = round(t % 3600 % 60 // 1)
        
        return [h, m, s]
