def explode(s):
    new_string = ""
    for i in s:
        new_string += i * int(i)

    return new_string
