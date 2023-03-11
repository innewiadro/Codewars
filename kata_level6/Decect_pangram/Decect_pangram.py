import string

def is_pangram(s):
    new_set = set()
    set_of_ascii = set(list(string.ascii_lowercase))
    list_of_letter = list(s.lower())
    for i in list_of_letter:
        if i.isalpha():
            new_set.add(i)
            
    return new_set == set_of_ascii

