def fake_bin(x):
    list_of_strings = list(x)

    for i in range(len(x)):
        if int(list_of_strings[i]) >= 5:
            list_of_strings[i] = "1"
        else:
            list_of_strings[i] = "0"

    return "".join(list_of_strings)

def fake_bin_list_comprehension(x):
    list_of_strings = list(x)
    print([list_of_strings[i] if for i in range(len(x)) if int(list_of_strings[i]) >= 5 else list_of_strings[i] ])

    return

if __name__ == "__main__":
    print(fake_bin("456123"))
    print(fake_bin_list_comprehension("456123"))
