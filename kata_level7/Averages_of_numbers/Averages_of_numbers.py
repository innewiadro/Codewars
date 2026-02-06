def averages(arr):
    if arr is None or len(arr) < 2:
        return []

    result = []

    for i in range(len(arr) - 1):
        avg = (arr[i] + arr[i + 1]) / 2
        result.append(avg)

    return result