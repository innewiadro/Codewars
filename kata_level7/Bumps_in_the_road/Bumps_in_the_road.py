def bumps(road):
    number_of_bumps = 0

    for i in road:
        if i == "n":
            number_of_bumps += 1

    return "Car Dead" if number_of_bumps > 15 else "Woohoo!"
