def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i:
            counter += 1
    return counter

def count_sheeps(sheep):
    return sheep.count(True)
