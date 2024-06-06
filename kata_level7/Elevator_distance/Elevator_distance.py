def elevator_distance(array):
    res = 0
    start = array[0]
    for i in array[1:]:
        if i > start:
            change = i - start
            res += change
        else:
            change = start - i
            res += change
        start = i
    return res
