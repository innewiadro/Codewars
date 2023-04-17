def sum_array(arr):
    if arr == None:
        return 0
    if len(arr) < 3:
        return 0
    else:   
        b = sorted(arr)
        b.pop()
        a = b[1:]
        return sum(a)
