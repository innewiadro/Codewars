def any_(lst, func):
    if not lst:
        return False

    return any(func(item) for item in lst)
