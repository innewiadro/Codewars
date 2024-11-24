def riders(stations):
    range = 0
    riders = 1
    for i in stations:
        if range + i > 100:
            riders += 1
            range = i
        else:
            range += i
    return riders
