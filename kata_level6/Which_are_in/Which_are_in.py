def in_array(array1, array2):
    new_set = set()
    for i in range(len(array1)):
        for j in range(len(array2)): 
            if array1[i] in array2[j]:
                new_set.add(array1[i])
    return sorted(list(new_set))
