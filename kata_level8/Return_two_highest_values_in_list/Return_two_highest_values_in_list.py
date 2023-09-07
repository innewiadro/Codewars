def two_highest(arg1):
    if type(arg1) is not list:
        return False
    else:
        return sorted(list(set(arg1)), reverse=True)[:2]
