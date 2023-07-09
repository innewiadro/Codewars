def reverse_letter(string):
    return "".join(filter(lambda x: x.isalpha(), string))[::-1]
