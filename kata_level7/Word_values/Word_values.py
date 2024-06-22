def name_value(my_list):
    res_list = []
    number = 0

    for i in my_list:

        res = 0
        number += 1

        for j in i:

            if j == " ":
                continue

            res += ord(j) - 96

        res_list.append(res * number)

    return res_list
