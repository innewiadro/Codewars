def fold_to(distance):
    if distance < 0:
        return None

    x = 0.0001
    number = 0

    while distance > x:
        distance /= 2
        number += 1

    return number
