def ship_of_theseus(ship):
    if len(ship) <= 1:
        return True

    row_length = len(ship[0])
    for row in ship:
        if len(row) != row_length:
            return False

    for i in range(len(ship) - 1):
        differences = 0

        for a, b in zip(ship[i], ship[i + 1]):
            if a != b:
                differences += 1

        if differences != 1:
            return False

    return True