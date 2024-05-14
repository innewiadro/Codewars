def initialize_names(name):
    name_list = name.split(" ")
    first = name_list[0]
    last = name_list[-1]
    mid = " "

    if len(name_list) > 2:
        del name_list[0]
        del name_list[-1]
        for i in name_list:
            mid += i[0] + ". "

    return first + mid + last if first != last else name_list[0]
