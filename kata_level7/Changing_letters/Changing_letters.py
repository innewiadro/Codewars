def swap(st):
    string_c = ""
    for i in st:
        if i in "aeiou":
            string_c += i.upper()
        else:
            string_c += i
    return string_c
