def drop_while(arr, pred):
    return arr[next((i for i, x in enumerate(arr) if not pred(x)), len(arr)):]
