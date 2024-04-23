def smaller(arr):
    result = []
    start = 0
    for i in arr:
        counter = 0
        for j in arr[start:]:
            if i > j:
                counter += 1
        start += 1
        result.append(counter)

    return result
