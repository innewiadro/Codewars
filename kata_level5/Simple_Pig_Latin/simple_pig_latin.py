def pig_it(text):
    new_list = []
    list_of_white = "?!"
    for i in text.split():
        a = i[1:len(i)] + i[0] + "ay"
        if a[0] in list_of_white:
            a = a[0:1]

        new_list.append(a)

    return " ".join(b for b in new_list)
