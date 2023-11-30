def multiple_of_index(arr):
    new_list = []

    if arr[0] == 0:
        new_list.append(0)

    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            new_list.append(arr[i])
    return new_list
