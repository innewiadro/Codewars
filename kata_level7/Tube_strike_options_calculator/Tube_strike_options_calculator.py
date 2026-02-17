def calculator(distance, bus_drive, bus_walk):
    walk_time = distance / walk
    bus_time = (bus_walk / walk) + (bus_drive / bus)

    if walk_time > 2:
        return "Bus"

    if walk_time < (10 / 60):
        return "Walk"

    if walk_time <= bus_time:
        return "Walk"

    return "Bus"