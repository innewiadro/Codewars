def find_uniq(arr):
    uniqes = set(arr)
    for i in uniqes:
        arr.remove(i)
    return list(uniqes - set(arr))[0]
