def convert(degrees):
    deg = int(degrees)
    remainder = degrees - deg

    total_minutes = remainder * 60
    minutes = int(total_minutes)

    seconds = round((total_minutes - minutes) * 60)


    if seconds == 60:
        seconds = 0
        minutes += 1

    if minutes == 60:
        minutes = 0
        deg += 1

    result = [deg]

    if minutes != 0 or seconds != 0:
        result.append(minutes)

    if seconds != 0:
        result.append(seconds)

    return result