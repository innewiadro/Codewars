def split_in_parts(s, part_length):
    new_s = ""
    counter = 1

    for i in s:
        if counter % part_length == 0:
            new_s += i + " "
        else:
            new_s += i
        counter += 1
    return new_s if new_s[-1] != " " else new_s[:-1]
