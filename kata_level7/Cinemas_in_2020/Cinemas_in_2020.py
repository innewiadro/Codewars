def maximum_seating(seats):
    seats = seats[:]
    n = len(seats)
    count = 0

    for i in range(n):
        if seats[i] == 0:
            left_ok = (i == 0 or seats[i - 1] == 0) and (i < 2 or seats[i - 2] == 0)
            right_ok = (i == n - 1 or seats[i + 1] == 0) and (i > n - 3 or seats[i + 2] == 0)

            if left_ok and right_ok:
                seats[i] = 1
                count += 1
    return count
