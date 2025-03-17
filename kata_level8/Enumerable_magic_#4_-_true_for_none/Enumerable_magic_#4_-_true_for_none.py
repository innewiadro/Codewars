def none(lst, func):
    return all(not func(x) for x in lst)
