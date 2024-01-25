def split_and_merge(string, separator):
    sti = string.split(" ")
    x = ''
    for i in sti:
        i = separator.join(i)
        x = x + ' ' + i
    return x[1:]
