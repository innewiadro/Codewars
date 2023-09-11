def replace_exclamation(s):
    string = ""
    for i in s:
        if i in "aeiouAEIOU":
            string += "!"
        else:
            string += i
    return string
