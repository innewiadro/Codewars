def jumping_number(number):
    int_list = [int(i) for i in list(str(number))]
    b = 1
    for digit in int_list[:-1]:
        if abs(digit - int_list[b]) != 1:
            return "Not!!"
        b += 1

    return "Jumping!!"
