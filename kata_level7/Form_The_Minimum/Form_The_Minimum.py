def min_value(digits):
    seta = set(digits)
    string = ""
    a = len(seta)
    for i in range(a):
        string += str(min(seta))
        seta.remove(min(seta))
    return int(string) 
