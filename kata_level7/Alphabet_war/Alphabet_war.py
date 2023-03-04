def alphabet_war(fight):
    right_side = 0
    left_side = 0
    for char in fight:
        if char == "w":
            left_side += 4
        if char == "p":
            left_side += 3
        if char == "b":
            left_side += 2
        if char == "s":
            left_side += 1

    for char in fight:
        if char == "m":
            right_side += 4
        if char == "q":
            right_side += 3
        if char == "d":
            right_side += 2
        if char == "z":
            right_side += 1

    if right_side > left_side:
        return "Right side wins!"

    elif right_side < left_side:
        return "Left side wins!"
    else:
        return "Let's fight again!"
