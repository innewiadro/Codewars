def vowel_2_index(strings):
    abc = "aeiou"
    number = 1
    new_string = ""
    for i in strings:
        if i.lower() in abc:
            new_string += str(number)
        else:
            new_string += i

        number += 1
    return new_string
