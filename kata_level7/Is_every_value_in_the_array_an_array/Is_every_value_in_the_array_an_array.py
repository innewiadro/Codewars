def arr_check(arr):
    return all(isinstance(item, list) for item in arr)