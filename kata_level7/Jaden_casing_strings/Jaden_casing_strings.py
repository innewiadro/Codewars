def to_jaden_case(string):
    a= []
    list_from_string = string.split()
    for i in list_from_string:
        a.append(i.capitalize())
        
    return " ".join(a)
