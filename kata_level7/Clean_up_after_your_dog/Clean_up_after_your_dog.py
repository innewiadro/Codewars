def crap(garden, bags, cap):
    res = 0

    for row in garden:
        for item in row:
            if item == 'D':
                return "Dog!!"
            elif item == '@':
                res += 1

    total = bags * cap

    if bags == 0:
        return "Cr@p"

    if bags == 0:
        return "Cr@p"

    if res <= total:
        return "Clean"
    else:
        return "Cr@p"
