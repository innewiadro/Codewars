def is_sorted_and_how(arr):
    if arr == sorted(arr, reverse=False):
        return 'yes, ascending'
    elif arr == sorted(arr, reverse=True):
        return 'yes, descending'
    else:
        return "no"
