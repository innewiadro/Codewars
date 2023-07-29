def first_non_repeating_letter(string):
    list_of_letter = [letter.lower() for letter in string]
    for i in range(len(list_of_letter)):
        if list_of_letter.count(list_of_letter[i]) == 1:
            return string[i]
    return ""
