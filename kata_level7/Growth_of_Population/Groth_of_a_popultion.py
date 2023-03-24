def nb_year(p0, percent, aug, p):
    count_year = 0
    while p > p0:
        p0 = p0 + int(p0 * percent / 100) + aug
        count_year += 1

    return count_year
