def scratch(lottery):
    total = 0

    for ticket in lottery:
        parts = ticket.split()
        animals = parts[:3]
        prize = int(parts[3])

        if animals[0] == animals[1] == animals[2]:
            total += prize

    return total
