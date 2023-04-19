def get_length_of_missing_array(array_of_arrays):
    if None in array_of_arrays or not array_of_arrays:
        return 0
    
    a = sorted(array_of_arrays, key=len)
    
    if not all(a):
        return 0
    
    score = len(a[0])
    for i in range(0, len(a)):
        if len(a[i]) == len(a[0]) + i:
            score += 1
        else:
            return score
