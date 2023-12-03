def last(s):
    x_list = (s.split(' '))
    x_list.sort(key=lambda x:x[-1])
    return x_list
