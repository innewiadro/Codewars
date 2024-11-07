def snail(column, day, night):
    days = 0
    current_height = 0

    while True:
        days += 1
        current_height += day

        if current_height >= column:
            return days

        current_height -= night
