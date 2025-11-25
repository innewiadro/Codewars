def swap_head_tail(arr):
    n = len(arr)
    half = n // 2

    if n % 2 == 0:
        return arr[half:] + arr[:half]
    else:
        return arr[half + 1:] + [arr[half]] + arr[:half]
