def lowercase_count(string):
    number_of_lower = 0
    for i in string:
        if i.islower():
            number_of_lower += 1
    return number_of_lower
