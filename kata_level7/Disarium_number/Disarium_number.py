def disarium_number(number):
    sum_of_number = 0
    c = 1
    for i in str(number):
        sum_of_number += int(i) ** c
        c += 1

    return "Disarium !!" if sum_of_number == number else "Not !!"
