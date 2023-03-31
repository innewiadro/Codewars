def count(s):
    my_dict = {}
    if s == []:
        return {}
    for i in s:
        try:
            my_dict[i] += 1
        except:
            my_dict[i] = 1

    return my_dict
