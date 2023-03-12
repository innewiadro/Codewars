def accum(s):
    new_string = ""
    count = 0
    string_into_list = list(s)
    for i in string_into_list:
        new_string += i.upper() + i.lower() * count + "-"
        count += 1
    return new_string[:len(new_string) - 1]
