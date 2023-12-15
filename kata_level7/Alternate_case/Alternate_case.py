def alternate_case(s):
    string = ""
    for i in s:
        if i.isupper():
            string += i.lower()
        elif i.islower():
            string += i.upper()
        else:
            string += i
    return string
