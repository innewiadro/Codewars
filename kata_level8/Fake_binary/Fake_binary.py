def fake_bin(x):
    list_of_strings = list(x)

    for i in range(len(x)):
        if int(list_of_strings[i]) >= 5:
            list_of_strings[i] = "1"
        else:
            list_of_strings[i] = "0"

    return "".join(list_of_strings)

