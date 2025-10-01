def find_function(func,arr):
    fn = next(item for item in func if callable(item))
    return list(filter(fn, arr))
