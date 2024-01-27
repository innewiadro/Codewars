def capitalize(s, ind):
    number = 0
    string = ""
    for i in s:
        if number in ind:
            string += i.capitalize()
        else:
            string += i
        number += 1

    return string
