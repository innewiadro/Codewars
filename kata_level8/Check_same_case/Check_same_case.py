def same_case(a, b): 
    if a.isalpha() and b.isalpha():
        if a.islower() == b.islower():
            return 1
        else:
            return 0
    else:
        return -1
