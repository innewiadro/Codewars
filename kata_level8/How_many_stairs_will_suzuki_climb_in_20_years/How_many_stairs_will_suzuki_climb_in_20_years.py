def stairs_in_20(stairs):
    sum_stairs = 0
    for day in stairs:
        for j in day:
            sum_stairs += j
    twenty_years = sum_stairs * 20

    return twenty_years
