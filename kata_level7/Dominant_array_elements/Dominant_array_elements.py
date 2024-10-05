def solve(arr):
    domi_ele = [arr[-1]]

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > domi_ele[-1]:
            domi_ele.append(arr[i])

    return domi_ele[::-1]
