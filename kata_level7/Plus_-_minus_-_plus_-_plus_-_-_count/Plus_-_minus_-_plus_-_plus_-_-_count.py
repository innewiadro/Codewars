def catch_sign_change(lst):
    if not lst:
        return 0

    count = 0
    for i in range(1, len(lst)):
        if (lst[i-1] >= 0 and lst[i] < 0) or (lst[i-1] < 0 and lst[i] >= 0):
            count += 1

    return count
