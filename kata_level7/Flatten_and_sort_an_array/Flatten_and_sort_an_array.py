def flatten_and_sort(array):
    new = []
    for i in array:
        for j in i:
            new.append(j)
    return sorted(new)
