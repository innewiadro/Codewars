def special_number(number):
    for i in str(number):
        if i in "6789":
            return "NOT!!"
    return "Special!!"