def save(sizes, hd):
    res= 0
    number = 0
    for i in sizes:
        res += i
        if hd >= res:
            number += 1
    return number
