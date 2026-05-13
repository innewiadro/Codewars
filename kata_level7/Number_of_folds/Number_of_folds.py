def number_of_folds(n):
    count = 0
    grids = 1

    while grids < n:
        grids *= 2
        count += 1

    return count