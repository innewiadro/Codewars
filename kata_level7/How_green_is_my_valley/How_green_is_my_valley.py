def make_valley(arr):
    arr.sort(reverse=True)
    left_wing = arr[::2]
    right_wing = arr[1::2]
    return left_wing + right_wing[::-1]
