def camel_case(s):
    new_list = []
    for i in s.split(" "):
        new_list.append(i.capitalize())      
    return "".join(new_list)
