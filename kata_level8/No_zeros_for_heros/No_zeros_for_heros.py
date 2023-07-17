def no_boring_zeros(n):
    return int(str(n).rstrip("0")) if len(str(n)) > 1 else n 
