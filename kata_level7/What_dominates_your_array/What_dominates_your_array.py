def dominator(arr):
    if len(arr) > 0:
        lenght = len(arr)  
    else: 
        return -1
    for i in arr:
        if arr.count(i) > len(arr) / 2:
            return i
    return -1
