def shuffle_it(arr, *swaps):
    result = arr[:]
    for i, j in swaps:
        result[i], result[j] = result[j], result[i]
    return result
