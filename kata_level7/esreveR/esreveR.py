def reverse(lst):
    empty_list = list(lst)
    for i in lst:
        empty_list.insert(0, i)
        empty_list.pop(-1)
    return empty_list
