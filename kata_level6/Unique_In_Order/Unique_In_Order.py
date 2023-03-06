def unique_in_order(iterable):
    list_of_unique = []
    for i in iterable:
        i in list_of_unique[-1:] or list_of_unique.append(i)
    return list_of_unique
