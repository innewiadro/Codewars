def points(games):
    sum_points = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            sum_points += 3
        elif int(i[0]) > int(i[2]):
            sum_points += 1

    return sum_points
