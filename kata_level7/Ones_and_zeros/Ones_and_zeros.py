def binary_array_to_number(arr):
    u = 0
    count = 0
    for i in range(len(arr)-1, -1, -1,):
        if arr[count] == 1:
            u += 2 ** i
        count += 1
    return u
