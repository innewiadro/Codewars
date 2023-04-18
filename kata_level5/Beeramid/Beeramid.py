def beeramid(bonus, price):
    number_of_cans = bonus // price
    if number_of_cans > 0:
        piramid = 1
        counter = 0
        i = 2

        while number_of_cans >= piramid:
            alfa = i ** 2
            piramid += alfa
            i += 1
            counter += 1

        return counter

    else:
        return 0
