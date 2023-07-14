def consonant_count(s):
    number_of_con = 0
    for i in s:
        if i.isalpha() and i not in "aeiouAEIOU":
            number_of_con +=1
    return number_of_con
