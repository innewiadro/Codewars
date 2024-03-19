def difference_of_squares(n):
    big = 0
    small = 0
    for i in range(1, n + 1):
        small += i ** 2
        big += i
    big_sq = big ** 2

    return big_sq - small
