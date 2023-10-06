def disemvowel(string_):
    vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = []
    for letter in string_:
        if letter not in vovels:
            new_string.append(letter)
    return ''.join(new_string)
